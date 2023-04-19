import requests

def getData(url):
    '''
    make a get request to the url if it is a https url
    '''
    if url.startswith('https://'):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
            return None
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            return None
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            return None
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)
            return None
    else:
        print("Only https requests are allowed.")
        return None

# CWE-601: URL Redirection to Untrusted Site ('Open Redirect')
# CWE-311: Missing Encryption of Sensitive Data
# CWE-319: Cleartext Transmission of Sensitive Information
# CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')
# CWE-502: Deserialization of Untrusted Data
# CWE-535: Information Exposure Through Shell Error Messages
# CWE-829: Inclusion of Functionality from Untrusted Control Sphere
# CWE-835: Loop with Unreachable Exit Condition ('Infinite Loop')
# CWE-943: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
# CWE-1168: Improperly Protected Transport of Credentials
# CWE-1170: Use of Server-Side Request Forgery (SSRF)