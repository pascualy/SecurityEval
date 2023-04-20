import smtplib

def getSMTPConnection(smtp_server, smtp_port):
    '''
    create a SMTP connection and return it
    '''
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.ehlo()
        smtp_connection.starttls()
        return smtp_connection
    except Exception as e:
        print(f"Error: {e}")
        return None