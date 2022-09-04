# 메일 검색
from imap_tools import MailBox
from account import *
import smtplib
from email.message import EmailMessage

max_val = 3
applicant_list = []  # 지원자 리스트

print("1. 지원자 메일 조회")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번저장
    for msg in mailbox.fetch(limit=10, reverse=True):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            # print("순번:{} 전화번호:{}".format(index, phone))
            applicant_list.append((msg, index, phone))
            index += 1


print("2. 선정 / 탈락 메일 발송")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_  # 수신 메일 주소
        index = applicant[1]
        phone = applicant[2]

        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = "xx님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정 순번 {}번)".format(index)
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = "xx님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락 드리겠습니다. (대기 순번 {}번)".format(
                index - max_val)

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
