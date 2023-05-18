# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеиоуэюяыё'
print(len([letter for letter in word.lower() if letter in vowels]))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(int(sum([len(word) for word in sentence.split()]) / len(sentence.split())))
