# 메일 검색
from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD,
#               initial_folder="INBOX")

# 한번에 쓰기 - mailbox.logout() 이 필요없다.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True):  # 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 사람이 보낸 메일만 찾기
    # for msg in mailbox.fetch('(FROM jeongjui153@gmail.com)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 글자를 포함하는 메일 가져오기( 제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test")', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # 항상 작은 따옴표로 먼저 감싸야한다.
    # 띄어쓰기로 구분하여 test, mail 이라는 각각의 단어를 포함하는 메일을 찾게된다.

    # 제목정보만 가져오기.
    # for msg in mailbox.fetch('(SUBJECT "test")', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # 한글로 적으면 인코딩 에러가 뜬다.

    # 한글을 포함한 메일 필터링.
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 30-Apr-2022)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 14-Apr-2022)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # import time, print(time.strftime('%d-%b-%Y')) # 현재 날짜를 위 형식대로 출력.
    # import datetime , dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d") , print(dt.strftime('%d-%b-%Y'))

    # 두개 이상의 조건을 모두 만족
    # for msg in mailbox.fetch('(ON 3-Jun-2022 SUBJECT "test")', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 둘중 하나라도 만족
    for msg in mailbox.fetch('(OR ON 3-Jun-2022 SUBJECT "test")', limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))
