import pymysql

try:
    con = pymysql.connect(host='localhost', port=3306,
                          user='root', password='1234',
                          db='mysql', charset='utf8')
    cursor = con.cursor()
    cursor.execute("update contact set phone='01011112222' where num=1")

except Exception as e:
    print(e)

finally:
    con.commit()
    con.close()
