# 파일 하나 만들어 보기.

# 먼저 설치
# pip install openpyxl
from openpyxl import Workbook
wb = Workbook()  # 새 워크북을 생성. 엑셀로 치면 새로운 창 연것.
ws = wb.active  # 현재 활성화된 sheet 가져옴.
ws.title = "lee"  # 워크시트의 이름을 변경.
# wb가 하나의 엑셀 파일이고 ws는 시트이다.
wb.save("sample.xlsx")  # 이 이름으로 엑셀 저장
wb.close()  # 파일 닫아주기.
