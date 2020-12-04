# Scratch
#!/usr/bin/env python3
import os
import smtplib
import imghdr
from email.message import EmailMessage

Email_Address = os.environ.get('DB_USER')
Email_Password = os.environ.get('DB_PASS')

msg = EmailMessage()
msg['Subject'] = 'INGENIOUS PRINTS'
msg['From'] = Email_Address
msg['To'] = 'm_ashfaque@hotmail.com'
msg.set_content('IMAGE ATTACHED')

#TO ADD HTML TEXT:
#msg.add_alternative("""\
#<!DOCTYPE html>
#<html>
#    <body>
#        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#    </body>
#</html>
#""", subtype='html')

#TO ATTACH SINGLE FILE:
#with open('D:\PICTURE\LOGO\y.jpg', 'rb') as f:
#    file_data = f.read()
#    file_type = imghdr.what(f.name)
#    file_name = f.name

#TO ATTACH MORE FILES:
files = ['D:\DOCUMENT\CV\CV_2020.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()

#NOT REQ IF IT'S NOT IMAGE-
#        file_type = imghdr.what(f.name)

        file_name = f.name

#FOR PDF:
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#FOR MULTI IMAGE:
#    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#FOR SINGLE IMAGE:
#msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

#FOR TLS_ENCRYPTION:
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#with smtplib.SMTP('localhost', 1025) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()

#FOR SSL _ENCRYPTION:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Address, Email_Password)

#SIMPLE FORMAT MESSAGE:
#    subject = 'hi its a test mail'
#    body = 'hi how are u this is a automated mail'
#    msg = f'Subject: {subject}\n\n{body}'
#    smtp.sendmail(Email_Address, 'm_ashfaque@hotmail.com', msg)

    smtp.send_message(msg)
