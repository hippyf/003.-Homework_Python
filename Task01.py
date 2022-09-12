 # Задайте список из нескольких чисел. Напишите программу, 
 # которая найдёт сумму элементов списка, стоящих на нечётной позиции.

N = int(input('Количество чисел в списке: '))
spisok = []
summa = 0

for i in range(N):
    spisok.append(int(input(f'Введите {i+1} - й элемент списка ')))
for i in range(1, N, 2):
    summa += spisok[i]

print(summa)
