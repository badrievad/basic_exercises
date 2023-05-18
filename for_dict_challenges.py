import pandas as pd
from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for student in students:
    names.append(student['first_name'])

for key, value in Counter(names).items():
    print(f'{key}: {value}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for student in students:
    names.append(student['first_name'])

print('_' * 75)

# print(pd.DataFrame(names).mode()[0][0])
print(f'Самое частое имя среди учеников: {max(names, key=lambda x: names.count(x))}')

print('_' * 75)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for key, value in dict(enumerate(school_students, start=1)).items():
    print(f'Самое частое имя в классе {key}: '
          f'{(lambda x: max([x["first_name"] for x in value], key=lambda y: x.count(y)))(value)}')

print('_' * 75)
# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for group in school:
    print(f'Класс {group["class"]}: девочки '
          f'{(lambda x: [is_male[x["first_name"]] for x in group["students"]])(group).count(False)}, мальчики '
          f'{(lambda x: [is_male[x["first_name"]] for x in group["students"]])(group).count(True)}')

print('_' * 75)

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
girls_boys = []
for group in school:
    girls_boys.append({
        'class': group['class'],
        'girls': (lambda x: [is_male[x["first_name"]] for x in group["students"]])(group).count(False),
        'boys': (lambda x: [is_male[x["first_name"]] for x in group["students"]])(group).count(True)
    })

print(f"Больше всего мальчиков в классе: {max(girls_boys, key=lambda x: x['boys'])['class']}")
print(f"Больше всего девочек в классе: {max(girls_boys, key=lambda x: x['girls'])['class']}")
