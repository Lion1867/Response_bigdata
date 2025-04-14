import sys
from itertools import groupby
from operator import itemgetter

def reducer():
    # Чтение данных из stdin и сортировка по ключу (userid)
    data = [line.strip().split('\t') for line in sys.stdin]
    data.sort(key=itemgetter(0))  # Сортируем по userid

    # Группировка по userid
    for userid, group in groupby(data, key=itemgetter(0)):
        activities = [float(userid_activity[1]) for userid_activity in group]  # собираем все активности
        avg_activity = sum(activities) / len(activities)  # вычисляем среднюю активность
        print(f"{userid}\t{avg_activity}")

if __name__ == '__main__':
    reducer()
