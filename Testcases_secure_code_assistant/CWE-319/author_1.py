import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def getSMTPConnection(smtp_server, smtp_port, smtp_username, smtp_password):
    '''
    create a secure SMTP connection and return it
    '''
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(smtp_username, smtp_password)
        return server
    except Exception as e:
        print(f"Error: {e}")
        return None

def sendEmail(smtp_server, smtp_port, smtp_username, smtp_password, from_email, to_email, subject, message, attachment=None, image=None):
    '''
    send an email with optional attachment and image
    '''
    server = getSMTPConnection(smtp_server, smtp_port, smtp_username, smtp_password)
    if server is not None:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        if attachment is not None:
            with open(attachment, 'rb') as f:
                attach = MIMEApplication(f.read(), _subtype='pdf')
                attach.add_header('Content-Disposition', 'attachment', filename=f.name)
                msg.attach(attach)
        if image is not None:
            with open(image, 'rb') as f:
                img = MIMEImage(f.read(), name=f.name)
                msg.attach(img)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()