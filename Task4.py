# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите N: '))
list1 = []

for i in range(-N, N+1):
    list1.append(i)
print(list1)

with open('file.txt', "w") as file:
    file.write('1 \n')
    file.write('3 \n')
    file.write('4 \n')
    file.write('-2 \n')
    file.write('-1 \n')
file.close()

positions = 'file.txt'
file = open(positions, 'r')

mult_pos = 1
for string in file:
    pos = int(string)
    mult_pos *=list1[pos]
print(mult_pos)