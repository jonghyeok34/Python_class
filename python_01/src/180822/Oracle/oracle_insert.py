# dept 테이블에 데이터 입력

import cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
    cursor = con.cursor()
    data1 = input("부서번호")
    data2 = input("부서위치")
    data3 = input("부서업무")
    sql = "insert into dept values({0},'{1}','{2}')".format(data1, data2, data3)
    cursor.execute(sql)
except Exception as e:
    print('데이터 베이스 연결 실패')
    print(e)
finally:
    con.commit()
    cursor.close()
    con.close()
