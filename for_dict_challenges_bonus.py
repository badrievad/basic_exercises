import random
import uuid
import datetime
import lorem
from itertools import groupby
from collections import Counter

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


# Создадим функцию, которая принимает list для нахождения максимального повторяющегося элемента в данном списке
def maximum_frequency(lst):
    return Counter(lst).most_common(1)[0][0]


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


# Создает список значений по ключу
def create_list_by_key(key_name: str, messages):
    return [message[key_name] for message in messages if message[key_name] is not None]


def find_id_who_write_the_most_messages(messages):
    return maximum_frequency(create_list_by_key('sent_by', messages))


def find_id_who_got_the_most_replies(messages):
    for message in messages:
        if message['id'] == maximum_frequency(create_list_by_key('reply_for', messages)):
            return message["sent_by"]


def find_id_saw_unique_users(messages):
    id_unique = {}
    for message in messages:
        if message['sent_by'] not in id_unique:
            id_unique[message['sent_by']] = set(message['seen_by'])
        else:
            id_unique[message['sent_by']] = set(id_unique[message['sent_by']]) | set(message['seen_by'])

    # создаем переменную с отсортированными айди по убыванию кол-ва просмотров уникальными пользователями
    sorted_id_user_and_count_saw_users = sorted(id_unique.items(), reverse=True, key=lambda x: len(x[1]))
    return [id_user for id_user, count in sorted_id_user_and_count_saw_users]


def what_time_more_messages(messages):
    times = {
        'morning': [],
        'day': [],
        'evening': []
    }

    for message in messages:
        hour_of_writing = message["sent_at"].hour
        if hour_of_writing < 12:
            times['morning'].append(hour_of_writing)
        elif 18 > hour_of_writing > 12:
            times['day'].append(hour_of_writing)
        else:
            times['evening'].append(hour_of_writing)

    return max(times.items(), key=lambda x: len(x[1]))[0]


def maximum_thread_length(messages):
    result = []

    for id_reply_for, thread_length in groupby(
            [message['reply_for'] for message in messages if message['reply_for'] is not None]):
        length = len(list(thread_length))
        if length > 1:
            result.append(id_reply_for)

    return result


if __name__ == "__main__":
    print(find_id_who_write_the_most_messages(generate_chat_history()))
    print('_' * 75)
    print(find_id_who_got_the_most_replies(generate_chat_history()))
    print('_' * 75)
    print(find_id_saw_unique_users(generate_chat_history()))
    print('_' * 75)
    print(what_time_more_messages(generate_chat_history()))
    print('_' * 75)
    print(maximum_thread_length(generate_chat_history()))
