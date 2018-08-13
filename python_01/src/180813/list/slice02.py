# slice : 리스트 특정 구간에 있는 요소 추출
# [start index번호 : end-1 index번호]
# [1:4] index번호 1번 부터 3번까지 추출
# [4:] 4번 index부터 끝까지 추출
# [1::2] 1번 index부터 끝까지 2를 간격으로 출력

listdata = list(range(1, 21))  # 1,2,3, ... 19,20
print(listdata)

evenlist = listdata[1::2]
oddlist = listdata[0::2]

print(listdata)
print("짝수:", evenlist)
print("홀수:", oddlist)