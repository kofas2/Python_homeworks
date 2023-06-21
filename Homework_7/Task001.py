# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам    Парам пам-пам

def vowel_count(my_str):
    vowel_list = [ 'а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for i in my_str:
        if i in vowel_list: count +=1
    return count

# poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
sign = input('введите стих: ')
sign = sign.split()
if len(set(map(vowel_count,sign))) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам') 