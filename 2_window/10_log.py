# 로그를 남기는 방법.
# 프로그램 실행중 파일이나 로그를 남겨 나중에 확인할수 있다.
# import logging

# logging.basicConfig(level= logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# # 기본세팅, 로그 레벨 = 디버그 레벨 이상의 모든 로그 찍기, 포멧은 로그를 어떻게 찍을것인지 지정
# # 로그 시간정보, 로그가 어떤 레벨인지(디버그, 에러,...), 메시지

# # 로그 찍기.
# logging.debug("아 이거 누가 짠거야") # 개발자만 보도록
# logging.info("자동화 수행 준비") # 사용자도 보도록
# logging.warning("이 스크립트는 오래되었습니다.")
# logging.error("에러가 발생")
# logging.critical("심각한 문제") # 치명적인것 발생
# # 로그 레벨 순서 debug < info < warning < error < critical
# # 디버그가 제일 작다. 

# 파일도 함께 남기기.
# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
logFomatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") # 해당 형태로 로그를 작성
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림(터미널)에 로그 출력
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFomatter)
logger.addHandler(streamHandler)

# 파일에도 남기기
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # 파일만들기
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFomatter)
logger.addHandler(fileHandler)

logger.debug("로그 남기는 테스트")


