# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum = int(input("Введите количество журавликов: "))
if sum%3 == 0 and sum%2 == 0:
    katya = int((sum*2)/3)
    petya = int(katya//4)
    sergey = petya
    print("Петя сделал ", petya, " журавлик(ов)")
    print("Катя сделала ", katya, " журавликов")
    print("Петя сделал ", sergey, " журавлик(ов)")
else: 
    print("Неверное количество журавриков!!!")
