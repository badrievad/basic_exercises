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


# функция принимает число и изменяет существительное "группа" в зависимости от переданного аргумента
def singular_and_plural_noun_group(numb):
    if numb in range(5, 20):
        return 'групп'
    elif 1 in (numb, (diglast := numb % 10)):
        return 'группа'
    elif {numb, diglast} & {2, 3, 4}:
        return 'группы'
    return 'групп'


# функция принимает число и изменяет существительное "ученик" в зависимости от переданного аргумента
def singular_and_plural_noun_student(numb):
    if numb in range(5, 20):
        return 'учеников'
    elif 1 in (numb, (diglast := numb % 10)):
        return 'ученик'
    elif {numb, diglast} & {2, 3, 4}:
        return 'ученика'
    return 'учеников'


print(f'Всего {len(groups)} {singular_and_plural_noun_group(len(groups))}.')

for group_number, group in enumerate(groups, start=1):
    print(f'Группа {group_number}: {len(group)} {singular_and_plural_noun_student(len(group))}.')

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

for group_number, group in enumerate(groups, start=1):
    print(f'Группа {group_number}: {", ".join(group)}')
