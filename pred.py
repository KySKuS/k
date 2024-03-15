'''import csv
with open('students.csv', encoding="utf8") as csvfile:
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
answer = list(reader)[1:]
for id, name, titleProject_id, level, score in answer:
if 'Хадаров Владимир' in name:
print(f"Ты получил: {score}, за проект - {titleProject_id}")
break
count_class = {}
sum_class = {}
for el in answer:
count_class[el[-2]] = count_class.get(el[-2], 0) + 1
sum_class[el[-2]] = count_class.get(el[-2], 0) + (int(el[-1]) if

el[-1] != 'None' else 0)
for el in answer:
if el[-1] == 'None':
el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open('students_new.csv', 'w', newline='', encoding='utf-8') as file:
w = csv.writer(file)
w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
w.writerows(answer)'''
#2
'''import csv

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
break'''
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
id_project = input()'''

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
w.writerows(students_passwords)'''


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
w.writerows(students_with_hash)'''
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
