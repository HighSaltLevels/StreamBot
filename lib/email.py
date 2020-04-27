import os
import smtplib
from email.mime.text import MIMEText

def send_failure(password, error):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('swdrummer13', password)

    body = f'StreamBot crashed!\n{error}'
    msg = MIMEText(body)
    msg['Subject'] = 'StreamBot Crashed!'
    msg['From'] = 'Me'
    msg['To'] = 'davidgreeson13@gmail.com'

    server.send_message(msg)
    server.quit()
#    os.systme('reboot')
