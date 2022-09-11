#Реализуйте алгоритм перемешивания списка.

from random import randint

N = int(input('Введите N: '))
min = int(input('Введите min: '))
max = int(input('Введите max: '))
list = []

for i in range(N):
    list.append(randint(min, max))
print('The original list is: ' + str(list))

for i in range(len(list)-1, 0, -1):
    j = randint(0, i+1)
    list[i], list[j] = list[j], list[i]
print('The shuffled list is: ' + str(list))
