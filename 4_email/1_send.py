# 구글 계정 2단계 인증 해야함.
# 맥용 앱 비밀번호를 발급받자
# 메일 발신 기본
import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:  # smtp 주소, 포트번호
    smtp.ehlo()  # 연결 수립 확인
    smtp.starttls()  # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # 로그인 작업 수행

    # 메일 보내기

    subject = "TEST MAIL"  # 메일 제목
    body = "MAIL BODY"  # 메일 본문
    # 한글로 보내려면 아스키 인코딩 에러가 뜬다.

    msg = f"Subject: {subject}\n{body}"  # 해당 형식 존재.
    # 보내는사람, 받는사람, 보낼 메시지
    smtp.sendmail(EMAIL_ADDRESS, "jeongjui153@gmail.com",
                  msg)
