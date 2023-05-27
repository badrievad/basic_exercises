from collections import Counter


# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

# создадим функцию, которая возвращает список студентов по ключу 'first_name'
def get_students_first_names(student_list):
    return [student['first_name'] for student in student_list]


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

for name, count_students in Counter(get_students_first_names(students)).items():
    print(f'{name}: {count_students}')

print('_' * 75)

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


# Создадим функцию, которая принимает list для нахождения максимального повторяющегося элемента в данном списке
def maximum_frequency(lst):
    return Counter(lst).most_common(1)[0][0]


print(f'Самое частое имя среди учеников: {maximum_frequency(get_students_first_names(students))}')

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

for class_number, students in enumerate(school_students, start=1):
    print(f'Самое частое имя в классе {class_number}: {maximum_frequency(get_students_first_names(students))}')

print('_' * 75)


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

def find_count_girls(students_group):
    return [is_male[girls["first_name"]] for girls in students_group["students"]].count(False)


def find_count_boys(students_group):
    return [is_male[boys["first_name"]] for boys in students_group["students"]].count(True)


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
    print(f'Класс {group["class"]}: девочки {find_count_girls(group)}, мальчики {find_count_boys(group)}')

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

list_with_classes_and_boys = []
list_with_classes_and_girls = []

for group in school:
    list_with_classes_and_girls.append((group["class"], find_count_girls(group)))
    list_with_classes_and_boys.append((group["class"], find_count_boys(group)))

print(f"Больше всего девочек в классе {max(list_with_classes_and_girls, key=lambda x: x[1])[0]}")
print(f"Больше всего мальчиков в классе {max(list_with_classes_and_boys, key=lambda x: x[1])[0]}")
