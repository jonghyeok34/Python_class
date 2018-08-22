# 회원정보 출력

import sqlite3

# 데이터 베이스 연결
con = sqlite3.connect('naverDB')
cur = con.cursor()

cur.execute('select * from user')

print('사용자ID 사용자이름 이메일 출생연도')
print('-------------------------------')

while True:
    row = cur.fetchone()
    if row == None: break

    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]

    print('%5s %15s %15s %5s' % (data1, data2, data3, data4))
