from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active


ws.delete_rows(8)  # 7번 학생 데이터 삭제
ws.delete_rows(3, 3)  # 3번째 줄에서 총 3줄을 삭제
# column도 마찬가지.
wb.save("sample_delete.xlsx")
