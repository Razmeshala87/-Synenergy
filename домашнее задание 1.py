#Задание №1
#Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники. Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, его возраст и кличку, а потом выведет все эти данные в одно предложение. Например:
#Это желторотый питон по кличке "Каа". Возраст: 34 года.
#Решение:
print('Здравствуйте!')
n=input('Укажите тип Вашего питомца: ')
i=input('Укажите возраст Вашего питомца: ')
z=input('Укажите кличку Вашего питомца: ')
print('Это ' +n, 'кличка ' +z, '. Возраст ' +i, 'года.')
