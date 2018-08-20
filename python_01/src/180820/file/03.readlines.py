# readlines() : 줄 단위로 전체 텍스트 파일을 읽어오는 함수
with open("movie_quotes.txt", 'r') as file:
    # 파일의 끝에 도달하면 ''를 리턴

    lines = file.readlines()
    for line in lines:
        print(line, end='')
