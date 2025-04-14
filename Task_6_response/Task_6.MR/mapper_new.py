import sys

def mapper():
    # Чтение входных данных
    for line in sys.stdin:
        fields = line.strip().split(',')
        if len(fields) > 1:  # Пропуск пустых строк
            userid = fields[1]
            s_all = fields[4]  # Считаем, что s_all находится в 5-м столбце
            try:
                s_all = float(s_all)  # Преобразуем в число
                print(f"{userid}\t{s_all}")
            except ValueError:
                pass  # Если не можем преобразовать в число, пропускаем строку

if __name__ == '__main__':
    mapper()
