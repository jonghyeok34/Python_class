# 엑셀 파일 (stats_104102.xlsx) 읽어오기

import openpyxl

# 엑셀 파일 읽어오기
filename = 'stats_104102.xlsx'
book = openpyxl.load_workbook(filename)

# 첫번쨰 시트 추출
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출

data = []
for row in sheet.rows:
    data.append([row[0].value, row[9].value])
print(data)

# 불필요한 정보 제거
del data[0]
del data[1]
del data[2]

# 데이터 인구순으로 정렬
data = sorted(data, key=lambda x: x[1])
print(data)

# 인구수가 적은 도시 5개 출력
for i, a in enumerate(data):
    if i >= 5: break
    print(i + 1, a[0], int(a[1]))
