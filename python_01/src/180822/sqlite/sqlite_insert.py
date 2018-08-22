# user 테이블에 데이터 입력

import sqlite3

# 변수 선언
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""

# 데이터베이스 접속
con = sqlite3.connect('naverDB')

cur = con.cursor()

while True:
    data1 = input('ID 입력')
    # id를 입력하지 않고 Enter 키를 누르면 무한루프에서 빠져나옴.
    if data1 == '': break

    data2 = input('사용자 이름')
    data3 = input('email 주소')
    data3 = input('출생연도')

    sql = "insert into user values('{0}','{1}','{2}','{3}')".format(data1, data2, data3, data4)
    cur.execute(sql)

con.commit()
cur.close()
con.close()
