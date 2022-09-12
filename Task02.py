# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

N = int(input('Количество чисел в списке: '))
spisok = []
proisvedenie_par = []
j = (N - 1)
length = int(N / 2)

for i in range(N):
    spisok.append(int(input(f'Введите {i+1} - й элемент списка ')))

if N%2 == 1:
    for i in range((length + 1)):
        proisvedenie_par.append(int(spisok[i] * spisok[j]))
        j -= 1
else:
    for i in range(length):
        proisvedenie_par.append(int(spisok[i] * spisok[j]))
        j -= 1

print(proisvedenie_par)

