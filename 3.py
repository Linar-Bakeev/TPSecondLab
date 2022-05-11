import csv
import json
import os
import os.path as path


def convert_bytes(sz):
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if sz < 1024.0:
            return "%3.1f %s" % (sz, x)
        sz /= 1024.0


def get_files_sizes(p):
    file_arr = os.listdir(p)
    for filename in file_arr:
        print(filename, '(', convert_bytes(path.getsize(p + '/' + filename)), ')')


get_files_sizes(os.getcwd())

csv_filename = input("Введите название csv-файла: ")

try:
    with open(csv_filename, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        result = []
        for row in reader:
            row['number'] = int(row['number'])
            result.append(row)
        for row in result:
            print(row)

        with open('Workers.json', 'w', encoding='utf8') as fp:
            fp.write(json.dumps(result, ensure_ascii=False))
            fp.close()

        sort_key = input("Введите ключ сортировки: ")
        if sort_key not in result[0]:
            raise NotImplementedError()
        result.sort(key=lambda r: r[sort_key])
        for row in result:
            print(row)
        # os.remove(csv_filename)
except FileNotFoundError:
    print("Ошибка: файл не найден")
except NotImplementedError:
    print("Ошибка: ключ не найден")
