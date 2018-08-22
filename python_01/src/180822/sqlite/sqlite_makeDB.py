import sqlite3


# 테이블 생성 위함 함수
def create_table():
    # 데이터 베이스 연결
    con = sqlite3.connect("naverDB")

    # 커서 생성
    cur = con.cursor()

    # user table 생성
    cur.execute('''create table user(
                        id char (20),
                        username_char(20),
                        email char(30),
                        birth char(20))'''
                )

    con.commit()
    con.close()


if __name__ == '__main__':
    create_table()
