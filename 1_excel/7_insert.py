# 엑셀에 빈줄이나 빈칸을 삽입.
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 파일 위치에서 삽입누르면 파일위치에 빈줄 생김
ws.insert_rows(8)  # 8번쨰 줄이 비워짐
ws.insert_rows(8, 5)  # 8번째 줄 위치에 5줄을 추가

ws.insert_cols(2, 3)

wb.save("sample_insert_rows.xlsx")
