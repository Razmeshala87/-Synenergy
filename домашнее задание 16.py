pets = {}
pets2 = {}
while(True):
    x = input("Введите имя питомца: ")
    if x == "":
        break
    else:
        x1 = input("Вид питомца: ")
        x2 = int(input("Возраст питомца: "))
        year_case = ""
        if x2 % 10 == 1 and x2 != 11 and x2 % 100 != 11:
            year_case = "год"
        elif 1 < x2 % 10 <= 4 and x2 != 12 and x2 != 13 and x2 != 14:
            year_case = "года"
        else:
            year_case = "лет"
        x3 = input("Имя владельца: ")

    pets2 = {"Вид питомца: " :x1, "Возраст питомца: " :x2, "Имя владельца: " :x3 }
    pets[x] = pets2
    print("Это", pets2["Вид питомца: "], "по кличке", pets.keys(), ". Возраст питомца:", pets2["Возраст питомца: "], year_case, "Имя владельца: ", pets2["Имя владельца: "])

