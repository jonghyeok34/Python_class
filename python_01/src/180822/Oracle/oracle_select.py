import cx_Oracle

# 계정연결
con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')

cursor = con.cursor()

# sql문 실행
cursor.execute('select * from dept')

# row = cursor.fetchone()  # 1개의 데이터를 구해옴
row = cursor.fetchall()  # 모든 데이터를 구해옴

print(row)

cursor.close()
con.close()
