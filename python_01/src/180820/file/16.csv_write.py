import csv, codecs

with codecs.open('test.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')

    writer.writerow(['ID', '이름', '가격'])
    writer.writerow(['1000', 'SD카드', '30000'])
    writer.writerow(['1001', '키보드', '10000'])
    writer.writerow(['1002', '마우스', '20000'])
