#Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество

N=int(input("Введите число N "))

k = 0

for i in range(N, N+1):

    s=int(input("Введите N целых чисел "))
    if s==0:
        k+=1
print(k)

