# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Enter the numbers of elements of the first set: '))
m = int(input('Enter the numbers of elements of the second set: '))
list_1 = []
list_2 = []
for i in range(n):
    list_1.append(int(input(f'Enter a number {i+1} of the first set: ')))
print(list_1)
for j in range(m):
    list_2.append(int(input(f'Enter a number {j+1} of the second set: ')))
print(list_2)
list_3 = []
for i in list_1:
    if i in list_2 and i not in list_3:
            list_3.append(i)
list_3.sort()
print('Intersection of two sets: ', list_3)