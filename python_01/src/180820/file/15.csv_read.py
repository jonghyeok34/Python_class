
import pandas as pd

data = pd.read_csv('list-utf8.csv', encoding='utf-8')
print(type(data))

print(data.shape)
print(data['ID'])
print(data['이름'])
print(data['가격'])
