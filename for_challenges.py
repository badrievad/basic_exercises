# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(*names, sep='\n')

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}: {len(name)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(f'{name}: {"мужской" if is_male[name] else "женский"}')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

group_token = lambda group_to: (
        (group_to in range(5, 20)) and 'групп' or
        (1 in (group_to, (diglast := group_to % 10))) and 'группа' or
        ({group_to, diglast} & {2, 3, 4}) and 'группы' or 'групп')

student_token = lambda student_to: (
        (student_to in range(5, 20)) and 'учеников' or
        (1 in (student_to, (diglast := student_to % 10))) and 'ученик' or
        ({student_to, diglast} & {2, 3, 4}) and 'ученика' or 'учеников')

print(f'Всего {len(groups)} {group_token(len(groups))}.')

for key, value in dict(enumerate(groups, start=1)).items():
    print(f'Группа {key}: {len(value)} {student_token(len(value))}.')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

for key, value in dict(enumerate(groups, start=1)).items():
    print(f'Группа {key}:', ", ".join(value))
