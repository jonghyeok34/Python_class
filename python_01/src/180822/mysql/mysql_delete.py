# 회원 정보 출력

import pymysql

try:
    con = pymysql.connect(host='localhost', port=3306,
                          user='root', password='1234',
                          db='mysql', charset='utf8')

    cursor = con.cursor()
    cursor.execute('delete from contact where num=1')

    print('회원 정보 삭제')
except Exception as e:
    print(e)

finally:
    con.commit()
    con.close()
