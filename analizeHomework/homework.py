import csv

path = '/Users/xii/LearningPython/analizeHomework/refer/202303_202303_연령별인구현황_월간 (3).csv'
f = open(fr'{path}', encoding='cp949')
data = csv.reader(f)

newRow = []

city = input('사시는 동네 이름을 작성해주세요 : ')
for row in data :
  if city in row[0]:
    for num in row[3:]:
      newRow.append(int(num.replace(',', '')))

print(newRow)

import matplotlib.pyplot as plt

plt.plot(newRow)