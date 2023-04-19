from ctypes import CDLL, c_int, POINTER, Structure, byref, cast, pointer
from ctypes.util import find_library

class PamHandle(Structure):
    """
    Wrapper class for pam handle structure
    """
    _fields_ = [
        ("handle", c_void_p)
    ]

class PamMessage(Structure):
    """
    Wrapper class for pam message structure
    """
    _fields_ = [
        ("msg_style", c_int),
        ("msg", c_char_p)
    ]

class PamResponse(Structure):
    """
    Wrapper class for pam response structure
    """
    _fields_ = [
        ("resp", c_char_p),
        ("resp_retcode", c_int)
    ]

class PamConv(Structure):
    """
    Wrapper class for pam conversation structure
    """
    _fields_ = [
        ("conv", CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p))
    ]

# Define the necessary PAM constants
PAM_PROMPT_ECHO_OFF = 1
PAM_SUCCESS         = 0

# Load the PAM library and set the argument and return types for pam_authenticate
libpam                    = CDLL(find_library("pam"))
pam_authenticate          = libpam.pam_authenticate
pam_authenticate.restype  = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        # Create a pointer to an array of n_messages PamResponse objects
        addr = (PamResponse * n_messages)()
        # Set the resp field in each PamResponse to password
        for i in range(n_messages):
            addr[i].resp = cast(password.encode('utf-8'), c_char_p)
            addr[i].resp_retcode = 0
        # Set the value of p_response to the address of the array of PamResponse objects
        p_response[0] = addr
        return PAM_SUCCESS

    # Create a PamHandle object
    handle = PamHandle()
    # Initialize the PamHandle object with the specified service name
    result = libpam.pam_start(service.encode('utf-8'), username.encode('utf-8'), pointer(PamConv(my_conv)), byref(handle))
    # If the initialization was successful, try to authenticate the user
    if result == PAM_SUCCESS:
        result = pam_authenticate(handle, 0)
    # Clean up the PamHandle object
    libpam.pam_end(handle, result)
    # Return True if the authentication was successful, False otherwise
    return result == PAM_SUCCESS