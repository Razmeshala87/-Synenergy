#В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
#Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.
N = int(input())
spisok = list()
for i in range(1, N + 1):
    spisok.append(int(input()))
spisok.reverse()
print(spisok)