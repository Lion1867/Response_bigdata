import sys

def mapper():
    for line in sys.stdin:
        fields = line.strip().split(',')
        if len(fields) > 1:  # Пропуск пустых строк
            courseid = fields[0]
            userid = fields[1]
            print(f"{courseid}\t{userid}")

if __name__ == '__main__':
    mapper()