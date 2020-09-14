"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv 

def main():
    user_list = [{'name' : 'John', 'age' : '51', 'job' : 'Janitor'},
            {'name' : 'Bob', 'age' : '34', 'job' : 'Policeman'},
            {'name' : 'Alice', 'age' : '27', 'job' : 'Pharmacist'},
            {'name' : 'Kate', 'age' : '43', 'job' : 'Teacher'}]
    for user in user_list:
        print(user['name'])
    with open('user_list.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
