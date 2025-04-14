import sys

class MRCourseUniqueUsers:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def mapper(self, line):
        fields = line.strip().split(',')
        if len(fields) >= 2:
            courseid = fields[0]
            userid = fields[1]
            yield courseid, userid  

    def reducer(self, courseid, userids):
        unique_users = set(userids)  
        yield courseid, len(unique_users)

    def run(self):
        intermediate = {}
        with open(self.input_file, 'r', encoding='utf-8') as f:
            next(f)  # Пропуск заголовка
            for line in f:
                for key, value in self.mapper(line):
                    if key not in intermediate:
                        intermediate[key] = []
                    intermediate[key].append(value)

        results = {}
        for key, values in intermediate.items():
            for result_key, result_value in self.reducer(key, values):
                results[result_key] = result_value

        with open(self.output_file, 'w', encoding='utf-8') as f:
            for courseid, unique_count in sorted(results.items()):
                f.write(f"{courseid}: {unique_count}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python mr_userid.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    job = MRCourseUniqueUsers(input_file, output_file)
    job.run()
    print(f"Готово! Результат сохранён в {output_file}")
