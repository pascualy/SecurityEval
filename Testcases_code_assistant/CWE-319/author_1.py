import smtplib

def getSMTPConnection(smtp_server, port, username, password):
    '''
    create a SMTP connection and return it
    '''
    try:
        smtp_obj = smtplib.SMTP(smtp_server, port)
        smtp_obj.starttls()
        smtp_obj.login(username, password)
        return smtp_obj
    except Exception as e:
        print('Error:', e)