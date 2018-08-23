# contact 테이블에 데이터 입력

# create table contact(
#   num int auto_increment,
#   name varchar(100) not null,
#   phone varchar(20));

import pymysql

try:
    con = pymysql.connect(host='localhost', port=3306,
                          user='root', password='1234',
                          db='mysql', charset='utf8')
    cursor = con.cursor()
    cursor.execute("insert into contact(name,phone) values('kim','01011111111')")
except Exception as e:
    print(e)

finally:
    con.commit()
    con.close()