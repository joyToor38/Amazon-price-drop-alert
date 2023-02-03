import smtplib
import os
from email.message import EmailMessage

def notify(product, URL, TO_EMAIL_ID):

    EMAIL_ID = os.environ.get('TEST_E-MAIL')
    PASSWORD = os.environ.get('EMAIL_PASS')
    msg = EmailMessage()
    msg['Subject'] = "Price Drop Alert!!!"
    msg['From'] = EMAIL_ID
    msg['To'] = TO_EMAIL_ID
    msg.set_content(f"Hey, Price of {product} dropped!\n\n {URL}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ID, PASSWORD)
        smtp.send_message(msg)
        print(f"E-mail Sent to : {TO_EMAIL_ID}")
    

