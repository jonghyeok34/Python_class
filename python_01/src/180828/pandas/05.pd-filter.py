import pandas as pd

# 1차원 리스트가 들어있는 딕셔너리 자료형의 데이터가 있을 때 키(key)로 원하는 열의
# 데이터를 추출할 수 있다.
tbl = pd.DataFrame({
    "weight": [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
    "height": [170, 180, 155, 143, 154, 160],
    "gender": ["f", "m", "m", "f", "f", "m"]
})

print("--- height가 160 이상인 것")
print(tbl[tbl.height >= 160])

print("--- gender가 m 인 것")
print(tbl[tbl.gender == "m"])
