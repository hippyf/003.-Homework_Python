#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

N = int(input('Количество чисел в списке: '))
spisok = []
import random

for i in range(N):
    random_number = random.uniform(1.1, 20.5)
    spisok.append(round(random_number, 2))

print(spisok)

if spisok[0] - int(spisok[0]) < spisok[1] - int(spisok[1]):
    min = spisok[0] - int(spisok[0])
    max = spisok[1] - int(spisok[1])
else:
    min = spisok[1] - int(spisok[1])
    max = spisok[0] - int(spisok[0])

for i in spisok:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(round((max-min), 2))