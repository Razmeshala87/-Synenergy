#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».

#Для решения задачи создайте переменную и в неё положите слово с помощью input()

#А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

#Решение задания:

word = input("Введите слово: ")
a = word.count("a")
e = word.count("e")
i = word.count("i")
o = word.count("o")
u = word.count("u")

if a == 0:
    print("a = False")
if e == 0:
    print("e = False")
if i == 0:
    print("i = False")
if o == 0:
    print("o = False")
if u == 0:
    print("u = False")
print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {len(word) - (a + e + i + o + u)}")
