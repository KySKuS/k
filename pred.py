'''
import csv

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))
    # находим данные по Агафье
    for researcher in researchers_list:
        if 'Агафья' in researcher['Full_Name'] and 'Ершова' in researcher['Full_Name']:
            print(f'Вы получили {researcher["Prize"]} рублей в конкурсе {researcher["Nomination"]} с номером заявки {researcher["Project_id"]}.')
            break
    # считаем сумму призов и их количество по каждой номинации среди известных значений
    sums, counts = {}, {}
    for researcher in researchers_list:
        if researcher["Prize"] != 'NULL':
            sums[researcher['Nomination']] = sums.get(researcher['Nomination'], 0) + int(researcher['Prize'])
            counts[researcher['Nomination']] = counts.get(researcher['Nomination'], 0) + 1
    # заменяем неизвестные значения на средние в номинации
    for researcher in researchers_list:
        if researcher['Prize'] == 'NULL':
            researcher['Prize'] = round(sums[researcher['Nomination']] // counts[researcher['Nomination']], -3)

# записываем обновлённые значения в файл grants_new.csv
with open('grants_new.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(researchers_list)

'''
#2
'''
import csv

with open('students.csv', encoding="utf8") as csvfile:
reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
for i in range(len(reader)):

j = i - 1
key = reader[i]
while float(reader[j]['score'] if reader[j]['score'] != 'None'
else 0) < float(key['score'] if key['score'] != 'None' else 0) and j >= 0:

reader[j + 1] = reader[j]
j -= 1
reader[j + 1] = key

print('10 класс:')
count = 1
for el in reader:
if '10' in el['class']:
surname, name, patronymic = el["Name"].split()
print(f'{count} место: {name[0]}. {surname}')
count += 1
if count == 4:
break




import csv

def merge_sort(data):
    '''
    Функция сортировки методом слияния, осуществляющая разделение списка

    data – сортируемый список/массив
    '''
    if len(data) <= 1: return data
    mid = len(data) // 2
    left, right = merge_sort(data[:mid]), merge_sort(data[mid:])
    return merge(left, right, data)


def merge(left, right, merged):

    
    Вспомогательная функция для merge_sort, осуществляющая непосредственно слияние

    left, right – отсортированные списки/массивы, которые необходимо соединить
    merged – отсортированный результат слияния left и merged
    
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        left_value = int(left[left_cursor]['Prize']) if left[left_cursor]['Prize'] != 'NULL' else 0
        right_value = int(right[right_cursor]['Prize']) if right[right_cursor]['Prize'] != 'NULL' else 0
        if left_value >= right_value:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    merge_sort(researchers_list)

    top_position = 0
    print(f'Номинация: Проект будущего')
    for researcher in researchers_list:
        if researcher['Nomination'] == 'Проект будущего':
            top_position += 1
            name, patronymic, surname = researcher['Full_Name'].split()
            print(f'Топ-{top_position}: {surname} {name[0]}.')
            if top_position == 3: break

# with open('grants_sort.csv', 'w', encoding='cp1251') as file:
#     writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
#     writer.writeheader()
#     writer.writerows(researchers_list)
'''
#3
'''

import csv
with open('students_new.csv', encoding="utf8") as csvfile:
reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
data = sorted(reader, key=lambda x: x['titleProject_id'])

id_project = input()

while (id_project != 'СТОП'):
id_project = int(id_project)
for el in data:
if int(el['titleProject_id']) == id_project:
surname, name, patronymic = el["Name"].split()
print(f"Проект No{id_project} делал: {name[0]}. {surname} он(а)

получил(а) оценку - {el['score']}.")

break
else:
print('Ничего не найдено')
id_project = input()




import csv
# Linear search
with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    project_id = input()
    while project_id.lower() != 'стоп' and project_id != '':
        project_id = int(project_id)
        for researcher in researchers_list:
            if project_id == int(researcher['Project_id']):
                name, patronymic, surname = researcher['Full_Name'].split()
                prize = researcher["Prize"][:-3] if researcher['Prize'] != 'NULL' else 'NULL'
                print(f'Заявка № {project_id} Автор: {surname} {name[0]}.{patronymic[0]}. Сумма – {prize} тыс. руб.')
                break # если точно известно, что заявка уникальна (в файле, к сожалению, это не так)
        else:
            print('Такой заявки нет в реестре')
        project_id = input()

# Binary search
# with open('grants.csv', 'r', encoding='cp1251') as file:
#     researchers_list = list(csv.DictReader(file, delimiter=';'))
#     researchers_list = sorted(researchers_list, key=lambda x: int(x['Project_id']))


#     project_id = input()
#     while project_id.lower() != 'стоп' and project_id != '':
#         project_id = int(project_id)
        
#         left, right = 0, len(researchers_list) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if project_id == int(researchers_list[middle]['Project_id']):
#                 name, patronymic, surname = researchers_list[middle]['Full_Name'].split()
#                 print(f'Заявка № {project_id} Автор: {surname} {name[0]}.{patronymic[0]}. Сумма – {researchers_list[middle]["Prize"][:-3]} тыс. руб.')
#                 break # если известно, что заявка точно уникальна
#             elif project_id < int(researchers_list[middle]['Project_id']):
#                 right = middle - 1
#             else:
#                 left = middle + 1
#         else:
#             print('Такой заявки нет в реестре')
#         project_id = input()
'''

#4
'''
import csv
import string
import random
def create_initials (s):
names=s.split()
return f'{names[0]}_{names[1][0]}{names[2][0]}'
def create_password():
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(8))
return password
students_passwords=[]
with open('students.csv', encoding="utf8") as csvfile:
reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
for row in reader:
row['login']=create_initials(row['Name'])
row['password']=create_password()
students_passwords.append(row)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as file:
w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id',
'class', 'score', 'login', 'password'])
w.writeheader()
w.writerows(students_passwords)


import csv
import string
import random 

def create_login(fio):
    ''''''
    Функция создания логина пользователя по строке ФИО

    fio – строка с именем, отчеством и фамилией пользователя
    ''''''
    name, patronymic, surname = fio.split()
    return f'{name[0]}{patronymic[0]}{surname}'

def create_password():
    ''''''
    Функция генерации пароля по требованиям
    ''''''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    comma = '!?().'
    letters = lower + upper + digit + comma

    while True:
        password = ''.join(random.choices(letters, k=10))
        any_lower = any(char in password for char in lower)
        any_upper = any(char in password for char in upper)
        any_digit = any(char in password for char in digit)
        any_comma = any(char in password for char in comma)
        if any_lower + any_upper + any_digit + any_comma > 1: 
            return password

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    for researcher in researchers_list:
        researcher['Login'] = create_login(researcher['Full_Name'])
        researcher['Password'] = create_password()

with open('grants_auths.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize', 'Login', 'Password'])
    writer.writeheader()
    writer.writerows(researchers_list)
'''


#5
'''
import csv
def generate_hash(s):
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭ
ЮЯ '
d = {l: i for i, l in enumerate(str1,1)}
p = 67;
m = 1e9 + 9;
hash_value = 0;
p_pow = 1;
for c in s:
hash_value = (hash_value + d[c] * p_pow) % m;
p_pow = (p_pow * p) % m;
return int(hash_value)
students_with_hash=[]
with open('students.csv', encoding="utf8") as csvfile:
reader = list(csv.DictReader(csvfile, delimiter=',', quotechar='"'))
for row in reader:
row['id']=generate_hash(row['Name'])
print(row)
students_with_hash.append(row)

with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as
file:
w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id',
'class', 'score'])
w.writeheader()
w.writerows(students_with_hash)



import csv

def create_hash(s):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += ' '
    p, m = 67, 10**9 + 9  # 1e9 + 9
    hash = 0
    dictionary = {alphabet[i]: i + 1  for i in range(len(alphabet))}
    for i in range(len(s)):
        hash += dictionary[s[i]] * (i + 1)**2
    hash *= (p**(len(s)) - 1)
    hash += p
    return hash % m

with open('grants.csv', 'r', encoding='cp1251') as file:
    researchers_list = list(csv.DictReader(file, delimiter=';'))

    for researcher in researchers_list:
        researcher['id'] = create_hash(researcher['Full_Name'])

with open('grants_hash.csv', 'w', encoding='cp1251') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=['id', 'Full_Name', 'Project_id', 'Nomination', 'Prize'])
    writer.writeheader()
    writer.writerows(researchers_list)
'''
#quicksort
'''
def quicksort(alist, start, end):
    i = start
    j = end
    pivot = alist[(start+end)//2]
    
    while True:
        while alist[i] < pivot:
            i = i + 1 
        while alist[j] > pivot:
            j = j - 1     
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
            i = i + 1
            j = j - 1
        else:
            break
    
    if start < j:
        quicksort(alist,start,j)
    if i < end:
        quicksort(alist,i,end)

alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)
'''
#insertsort
'''
def insertion_sort(alist):
    for i in range(1, len(alist)):
        j = i
        while (j > 0 and alist[j] < alist[j-1]):
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j = j - 1

 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)
'''
