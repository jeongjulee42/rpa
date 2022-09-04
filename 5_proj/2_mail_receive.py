# 메일 검색
from imap_tools import MailBox
from account import *

applicant_list = []  # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1  # 순번저장
    for msg in mailbox.fetch(limit=10, reverse=True):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번:{} 전화번호:{}".format(index, phone))
            applicant_list.append((msg, index, phone))
            index += 1
