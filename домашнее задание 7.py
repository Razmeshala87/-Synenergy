#Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, 
#больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, 
#если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

#Решение задания:

min_cash = int(input("Минимальная сумма инвестиций: "))
cash_Mishael = int(input("У Майка: "))
cash_Ivan = int(input("У Ивана: "))

if (cash_Mishael >= min_cash) and (cash_Ivan >= min_cash):
    print(2)
elif (cash_Mishael >= min_cash) and (cash_Ivan<= min_cash):
    print("Mishael")
elif (cash_Mishael <= min_cash) and (cash_Ivan>= min_cash):
    print("Ivan")
elif (cash_Mishael <= min_cash) and (cash_Ivan<= min_cash) or ((cash_Mishael + cash_Ivan) >= min_cash):
    print(1)
else:
    print(0)

