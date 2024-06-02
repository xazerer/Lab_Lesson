# запросить текст у пользователя
text = input("введите текст: ").lower()

# подсчитать кол-во гласным
count = 0

for vowel in 'аеиоуюя':
    count += text.count(vowel)

# вывести результат:
print(count)