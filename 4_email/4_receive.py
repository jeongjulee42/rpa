# 메일 수신.
# pip install imap-tools
from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD,
              initial_folder="INBOX")  # 기본 편지함으로 선택

# mailbox.fetch() -> 전체 다가져오기 ,  limit- 최대 메일 개수, reverse - true 최근메일부터,
for msg in mailbox.fetch(limit=1, reverse=True):
    print(msg.subject)  # 제목
    print(msg.from_)  # 발신자.
    print(msg.to)  # 수신자.
    # print(msg.cc) # 참조자
    # print(msg.bcc) # 비밀 참조자
    print(msg.date)  # 날짜 정보
    # 1:49:23-07:00 -> 구글에서 gmt 검색해보기
    print(msg.text)  # 본문
    print(msg.html)  # html 메시지
    print("="*100)

    # 첨부파일
    for att in msg.attachments:
        print("첨부파일", att.filename)
        print(att.content_type)
        print(att.size)

        # 파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("다운로드 완료")


mailbox.logout()
