# ; Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# ; Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# ; В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# ; *Пример:*
# ; 5
# ; 1 2 3 4 5
# ; 3
# ; -> 1

n = int(input("Input list's lenght: "))

import random
nums = [random.randint(1,9) for i in range(n)]
print(nums)
x = int(input("Input number X: "))
count = 0
for i in range(n):
    if nums[i] == x:
        count += 1
print(f'Number X meets' , count, 'times')
