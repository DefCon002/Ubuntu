# Scratch
#!/usr/bin/env python3
import os
import pandas as pd
import smtplib
import xlrd

Email_Address = os.environ.get('DB_USER')
Email_Password = os.environ.get('DB_PASS')
My_Name = 'PYTHON'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Address, Email_Password)

    email_list = pd.read_excel("Email_List.xlsx")
    all_names = email_list['Name']
    all_emails = email_list['Email']
    all_subjects = email_list['Subject']
    all_messages = email_list['Message']

    for idx in range(len(all_emails)):

        name = all_names[idx]
        email = all_emails[idx]
        subject = all_subjects[idx]
        message = all_messages[idx]

        #full_email = ("From: {0} <{1}>\nTo: {2} <{3}>\nSubject: {4}\n\n{5}").format(My_Name, Email_Address, name, email, subject, message)
        full_email = (f"From: {My_Name} <{Email_Address}>\nTo: {name} <{email}>\nSubject: {subject}\n\n{message}")

        try:
            smtp.sendmail(Email_Address, [email], full_email)
            print(f'Email to {email} successfully sent!\n\n')

        except Excetion as e:
            print(f'Email to {email} could not be sent because {str(e)}\n\n')
            #print('Email to {} could not be sent because {}\n\n'.format(email, str(e)))