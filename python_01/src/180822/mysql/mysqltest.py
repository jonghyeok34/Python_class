import pymysql

# 데이터 베이스 연결

con = pymysql.connect(host='localhost', port=3306,
                      user='root', password='1234',
                      db='mysql', charset='utf8')

cursor = con.cursor()

cursor.execute('select * from user')

rows = cursor.fetchall()
print(type(rows))
print(rows)

con.close()