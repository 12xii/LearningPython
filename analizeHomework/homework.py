import csv

path = '/Users/xii/LearningPython/202303_202303_연령별인구현황_월간.csv'
f = open(fr'{path}', encoding='cp949')
data = csv.reader(f)

city = input('사시는 동네 이름을 작성해주세요 : ')
for row in data :
  if city in row[0]:
    for num in row[3:]:
      num = int(num.replace(',', ''))
      print(num)