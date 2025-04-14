import sys
from itertools import groupby
from operator import itemgetter

def reducer():
    # Чтение данных из stdin и сортировка по ключу (courseid)
    data = [line.strip().split('\t') for line in sys.stdin]
    data.sort(key=itemgetter(0))

    # Группировка по courseid
    for courseid, group in groupby(data, key=itemgetter(0)):
        userids = set(userid for _, userid in group)
        print(f"{courseid}\t{len(userids)}")

if __name__ == '__main__':
    reducer()