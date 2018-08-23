# 회원 정보 출력

import pymysql

try:
    con = pymysql.connect(host='localhost', port=3306,
                          user='root', password='1234',
                          db='mysql', charset='utf8')

    cursor = con.cursor()
    cursor.execute('select * from contact')

    rows = cursor.fetchall()
    for row in rows:
        print("%s. %s/ %s" % (row[0], row[1], row[2]))

except Exception as e:
    print(e)

finally:
    con.close()
