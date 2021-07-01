from openpyxl import load_workbook

wb = load_workbook("sample_formula.xlsx", data_only=True)
ws = wb.active

# 수식 그대로 가져오고 있음.
#for row in ws.values:
#    for cell in row:
#        print(cell)  #값이 아닌 수식이 뜸
        

# 수식이 아닌 실제 데이터를 가지고 옴
# 파일 열어서 저장 한번 해줘야지 None이 뜨지 않는다.
for row in ws.values:
    for cell in row:
        print(cell)
