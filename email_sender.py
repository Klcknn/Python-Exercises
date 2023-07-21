from email.message import EmailMessage  
from app2 import password
import ssl
import smtplib

email_sender = "kenanklc.76@gmail.com"
email_pasword = password
email_receiver = "derenol346@nmaller.com"
subject = "Herhangi bir başlık giriniz..."
body = """
    İçerik kısmını giriniz.

"""

email = EmailMessage()
email["From"] = email_sender
email["To"] = email_receiver
email["subject"] = subject
email.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_pasword)
    smtp.sendmail(email_sender, email_receiver, email.as_string())







