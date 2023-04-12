from ctypes import CDLL, c_int, POINTER, pointer, Structure, sizeof, byref
from ctypes.util import find_library

libpam = CDLL(find_library("pam"))

PAM_PROMPT_ECHO_OFF = 1

class PamMessage(Structure):
    _fields_ = [("msg_style", c_int),
                ("msg", c_char_p)]

class PamResponse(Structure):
    _fields_ = [("resp", c_char_p),
                ("resp_retcode", c_int)]

class PamConv(Structure):
    _fields_ = [("conv", POINTER(CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)))]

class PamHandle(Structure):
    _fields_ = [("handle", c_void_p)]

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

pam_end = libpam.pam_end
pam_end.restype = c_int
pam_end.argtypes = [PamHandle, c_int]

def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """
        for i in range(n_messages):
            if messages[i].msg_style == PAM_PROMPT_ECHO_OFF:
                pw_copy = password.encode('utf-8')
                resp = PamResponse(pw_copy, 0)
                p_resp = pointer(resp)
                p_response[i] = p_resp
        return 0

    handle = PamHandle()
    conv   = PamConv(byref(CFUNCTYPE(c_int, c_int, POINTER(PamMessage), POINTER(POINTER(PamResponse)), c_void_p)(my_conv)), None)

    pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv), POINTER(PamHandle)]
    retval = pam_start(service.encode('utf-8'), username.encode('utf-8'), byref(conv), byref(handle))

    if retval != 0:
        return False

    retval = pam_authenticate(handle, 0)

    pam_end(handle, retval)

    return retval == 0