import smtplib
from account import *
# 새로 import . 이전에는 메시지가 정해진 양식이어야만 전송이 가능. 한글도 문제. 이부분을 해결하는 방법.
from email.message import EmailMessage


# 이메일 객체 생성

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다."  # 제목
msg["From"] = EMAIL_ADDRESS  # 보내는사람
msg["To"] = "jeongjui153@gmail.com"  # 받는사람
# 여러명에게 보내기
# msg["To"] = "a, b, c, ... "
# to_list = [] 이렇게 리스트로 보낼사람 구성
# msg["To"] = ", ".join(to_list) # 리스트에 있는것들을 쉼표로 구분하여 합치는것.

# 참조
# msg["Cc"] = "e-mail"

# 비밀 참조
# msg["Bcc"] = "e-mail"

# 메시지(본문)
msg.set_content("테스트 본문입니다.")


# 이메일 보내기
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
