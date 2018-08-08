# 1~2월 중에 r이 들어있는 달 출력

# tuple
months = ('January', "February", "March", "April",
          "June", "July", "August", "September", "October",
          "November", "December")

for month in months:
    if 'r' in month:  # r찾기
        print(month)

