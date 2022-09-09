# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите N: '))
list1 = []
list2 = []
positions = ['1', '3', '6', '8']

for i in range(-N, N+1):
    list1.append(i)
print(list1)

with open('file.txt', "w") as file:
    for  string in positions:
        file.write(string + '\n')
