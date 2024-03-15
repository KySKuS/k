'''def read_rocket_file(month_num):
    # Открываем файл для чтения с указанием кодировки UTF-8
    with open("rocket_part.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()  # Читаем все строки из файла

    # Поиск строки с информацией о заданном месяце
    for line in lines:
        if month_num in line:
            return line  # Возвращаем строку с количеством шифров для указанного месяца

    return "В указанном месяце шифры не были получены."  # Если информации о месяце нет в файле

# Пример использования
input_month = input("Введите номер месяца (в формате 01, 02, ..., 12): ")
result = read_rocket_file(input_month.zfill(2))  # Запрос должен быть двухзначным числом
print(result)
''''''
def insertion_sort(signals):
    # Реализация сортировки вставками
    for i in range(1, len(signals)):
        key = signals[i]
        j = i - 1
        while j >= 0 and key["date"] < signals[j]["date"]:
            signals[j + 1] = signals[j]
            j -= 1
        signals[j + 1] = key

def print_earliest_signals(signals, n=3):
    # Вывод трех самых ранних сигналов
    print("Три самых ранних сигнала:")
    for signal in signals[:n]:
        print(f"Сигнал с шифром {signal['code']} был получен {signal['date']} и предназначается для {signal['rocketpart']}")

# Пример данных о сигналах (даты представлены строками в формате ДД.ММ.ГГГГ)
signals = [
    {"code": "001", "date": "10.05.2023", "rocketpart": "части ракеты A"},
    {"code": "002", "date": "15.04.2023", "rocketpart": "части ракеты B"},
    {"code": "003", "date": "25.04.2023", "rocketpart": "части ракеты C"},
    # Дополнительные данные о сигналах
]

insertion_sort(signals)  # Сортируем сигналы по дате
print_earliest_signals(signals)  # Выводим три самых ранних сигнала'''

'''
def binary_search(signals, key, category):
    # Двоичный поиск в массиве signals по ключу и категории
    left, right = 0, len(signals) - 1
    while left <= right:
        mid = (left + right) // 2
        if signals[mid]["date"] == key and signals[mid]["category"] == category:
            return mid
        elif signals[mid]["date"] < key or (signals[mid]["date"] == key and signals[mid]["category"] < category):
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример данных о сигналах
signals = [
    {"code": "001", "date": "2023-05-10", "rocketpart": "части ракеты A", "category": "category_1"},
    {"code": "002", "date": "2023-04-15", "rocketpart": "части ракеты B", "category": "category_2"},
    {"code": "003", "date": "2023-04-25", "rocketpart": "части ракеты C", "category": "category_1"},
    # Дополнительные данные о сигналах
]

# Отсортируем сигналы перед использованием двоичного поиска
signals.sort(key=lambda x: (x["date"], x["category"], x["code"]))

# Цикл для ввода и поиска шифра
while True:
    input_date = input("Введите дату (ГГГГ-ММ-ДД) или 'sleep' для завершения: ")
    if input_date == "sleep":
        break
    input_category = input("Введите категорию шифра: ")

    index = binary_search(signals, input_date, input_category)
    if index != -1:
        print(f"Шифр: {signals[index]['code']} от: {signals[index]['rocketpart']} был получен {signals[index]['date']}")
    else:
        print("В этот день космос молчал")
'''


import csv
from datetime import datetime

# Функция для генерации команды
def generate_command(date, code, module):
    command = ""
    
    # Преобразованный код: цифры -> буквы латиницы -> буквы кириллицы
    converted_code = ''.join(sorted(code, key=lambda x: (x.isdigit(), x.isalpha(), x)))

    # Разность годов: текущий год - год из значения даты
    curr_year = datetime.now().year
    date_year = int(date.split('-')[0])
    year_diff = curr_year - date_year

    # Генерация команды по правилам
    command = ' '.join([word[0].upper() for word in module.split()]) + " " + converted_code + " " + str(year_diff)
    return command

# Чтение данных из CSV файла и генерация команд
rocket_commands = []

with open("rocket.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок

    for row in reader:
        date, code, module = row
        command = generate_command(date, code, module)
        rocket_commands.append([date, command])

# Запись сгенерированных команд в новый файл rocket_commands.csv
with open("rocket_commands.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Дата", "Сгенерированная команда"])

    for command in rocket_commands:
        writer.writerow(command)

