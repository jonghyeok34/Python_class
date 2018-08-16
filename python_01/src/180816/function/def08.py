# 가변 매개변수가 있는 함수 정의 : **

# 가변 매개변수는 여러 개의 값을 입력 받을 수 있다.
# **를 이용해 정의된 가변 매개 변수는 입력 받은 값을 딕셔너리로 처리한다.

def print_team(**players):
    for k in players.keys():
        print("{}={}".format(k, players[k]))

# 함수 호출
print_team(손흥민='LW', 이승우='FW')
