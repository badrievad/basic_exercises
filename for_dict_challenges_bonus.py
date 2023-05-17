from collections import Counter
from itertools import groupby

"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem



def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def task1(messages):
    users_list = [message['sent_by'] for message in messages]
    return f'{max(users_list, key=lambda x: users_list.count(x))} - ' \
           f'айди пользователя, который написал больше всех сообщений'


def task2(messages):
    answers_list = [message['reply_for'] for message in messages if message['reply_for'] is not None]
    for i in messages:
        if i['id'] == max(answers_list, key=lambda x: answers_list.count(x)):
            return f'{i["sent_by"]} - айди пользователя, на сообщения которого больше всего отвечали'


def task3(messages):
    id_unique = {}
    for i in messages:
        if i['sent_by'] not in id_unique:
            id_unique[i['sent_by']] = i['seen_by']
        else:
            id_unique[i['sent_by']] = id_unique[i['sent_by']] + i['seen_by']

    for key, value in id_unique.items():
        print(f'Сообщения от пользователя под айди {key}, видело {len(set(value))} уникальных пользователей')


def task4(messages):
    d = {
        'утром (до 12 часов)': [],
        'днём (12-18 часов)': [],
        'вечером (после 18 часов)': []
    }

    for i in messages:
        if float(i["sent_at"].strftime('%H.%M')) < 12:
            d['утром (до 12 часов)'].append(float(i["sent_at"].strftime('%H.%M')))
        elif 18 > float(i["sent_at"].strftime('%H.%M')) > 12:
            d['днём (12-18 часов)'].append(float(i["sent_at"].strftime('%H.%M')))
        else:
            d['вечером (после 18 часов)'].append(float(i["sent_at"].strftime('%H.%M')))

    return f'В чате больше всего сообщений: {max(d, key=lambda x: len(d[x]))}'

def task5(messages):
    result = []

    for k, g in groupby([i['reply_for'] for i in messages]):
        length = len(list(g))
        result.append((k, length))

    lst = [(key, value) for key, value in sorted(result, key=lambda x: x[1], reverse=True) if
           key is not None and value > 1]

    if len(lst) > 0:
        for key, value in lst:
            print(f'Сообщение под айди: "{key}" стало началом для самых длинных тредов (цепочек ответов), а именно '
                  f'{value}.')
    else:
        print('Максимальная длина тредов (цепочек ответов) составляет 1.')

if __name__ == "__main__":
    print(task1(generate_chat_history()))
    print('_' * 75)
    print(task2(generate_chat_history()))
    print('_' * 75)
    task3(generate_chat_history())
    print('_' * 75)
    print(task4(generate_chat_history()))
    print('_' * 75)
    task5(generate_chat_history())
