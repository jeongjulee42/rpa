import smtplib
from account import *
from email.message import EmailMessage
import random

for i in range(5):
    msg = EmailMessage()
    msg["Subject"] = "파이썬 특강 신청합니다."
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "jeongjui153@gmail.com"
    msg_mail = """제목 : 파이썬 특강 신청합니다.
본문 : 나도코딩/{}""".format(random.randint(1000, 9999+1))
    msg.set_content(msg_mail)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
