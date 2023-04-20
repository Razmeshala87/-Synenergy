pets = {}
pets2 = {}
while(True):
    x = input("Введите имя питомца: ")
    if x == "":
        break
    else:
        x1 = input("Вид питомца: ")
        x2 = input("Возраст питомца: ")
        x3 = input("Имя владельца: ")

    pets2 = {"Вид питомца:":x1, "Возраст питомца:":x2, "Имя владельца:":x3 }
    pets[x] = pets2
        
for key, value in pets.items():
    view = value["Вид питомца: "]
    age = value["Возраст питомца: "]
    name = value["Имя владельца: "]
    year_case = ""
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        year_case = "год"
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        year_case = "года"
    else:
        year_case = "лет"
    print("Это", view, "по кличке", key, ". Возраст питомца:", age, year_case, "Имя владельца: ", name)

