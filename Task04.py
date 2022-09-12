#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
N = int(input('Введите число: '))
result = []

while N/2 > 0:
    result.append(N%2)
    N = int(N/2)
result.reverse()

print(result)
