# 1~12 월을 3자리 약어로 출력

# list
months = ['January', "February", "March", "April",
          "June", "July", "August", "September", "October",
          "November", "December"]


# for i in range(len(months)):
#     months[i] = months[i][0:3]  # 0~11
# print(months)

newMonth = []
for month in months:
    newMonth.append(month[0:3])
print(newMonth)
