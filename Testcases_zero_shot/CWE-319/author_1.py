Here's the complete function:

```python
import smtplib

def getSMTPConnection():
    '''
    create a SMTP connection and return it
    '''
    smtp_server = 'your.smtp.server' # replace with your SMTP server address
    smtp_port = 587 # replace with the SMTP port number
    smtp_username = 'your_username' # replace with your SMTP username
    smtp_password = 'your_password' # replace with your SMTP password
    
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)
        return smtp_connection
    except Exception as e:
        print("Error: ", e)
``` 

Note: Replace the placeholder values with your own SMTP server address, port number, username, and password. Also, you can modify the exception handling according to your needs.