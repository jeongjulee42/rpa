# 파일 참조
from fileinput import filename
import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."
msg["From"] = EMAIL_ADDRESS
msg["To"] = "jeongjui153@gmail.com"
msg.set_content("다운로드.")

# 첨부파일 등록
# msg.add_attachment()
# 파일을 읽어 파일의 내용을 직접 넣어줘야한다.
with open("img.png", "rb") as f:
    # 파일 내용을 읽어와서 보내줌/ 구글에 mime type 를 검색.
    msg.add_attachment(f.read(), maintype="image",
                       subtype="png", filename=f.name)
# pdf 의 경우 maintype="application" subtype="pdf"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
