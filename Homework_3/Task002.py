# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Input list's lenght: "))
import random
nums = [random.randint(1,9) for i in range(n)]
print(nums)
x = int(input("Input number X: "))
def nearval(nums, number):
    return min(nums, key=lambda x: abs(number - abs(x))) 
print(f'Number is nerby in list: {nearval(nums, x)}')