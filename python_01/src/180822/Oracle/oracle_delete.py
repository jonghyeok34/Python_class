import cx_Oracle

try:
    con = cx_Oracle.connect('scott.tiger@localhost:1521/xe')
    cursor = con.cursor()
    cursor.execute('delete from dept where deptno=50')

except Exception as e:
    print(e)
finally:

    con.commit()
    cursor.close()
    con.close()