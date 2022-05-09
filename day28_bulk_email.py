# ECX 30 DAYS OF CODE AND DESIGN
# Day 28

"""
**Bulk E-mail**

Using the built-in SMTP module, write a function that takes a list of emails as input,
and sends each of them an(any) email message.
"""

import smtplib
from email.message import EmailMessage

try:
    sender_email = input('Enter email: ')
    sender_password = input('Enter password: ')

    msg = EmailMessage()
    msg['Subject'] = 'Test Email From Python'
    msg['From'] = sender_email
    msg['To'] = ['favour.pytest@gmail.com', 'favour-olumese@live.unilag.edu.ng']
    msg.set_content('''\
    Good day,
    
    This is a test on the usage of python smtplib module in sending emails
    
    Yours faithfully,
    Test Email 
    ''')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_email, sender_password)

        smtp.send_message(msg)

except smtplib.SMTPAuthenticationError:
    print('Wrong password or email.')

except smtplib.SMTPConnectError:
    print('Error connecting to service')
