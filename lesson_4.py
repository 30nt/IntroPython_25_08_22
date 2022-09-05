# функция input
# обработка ошибок
# тернарный оператор
# цикл с условием
# методы строк

value = input("Введи целое число: ")
try:
    value = int(value)
    result = 1 / value
    print(value, result)
except (ValueError, TypeError):
    print("Это не целое число!!!")
except ZeroDivisionError:
    print("На ноль делить нельзя!!!")


################ тернарный оператор

value = -12
# #################
if value >= 0:
    result = value
else:
    result = value * 2
print(result)
# #################
result = value if value >= 0 else value * 2
print(result)
# новая_переменная = знач_если_да if условие else знач_если_нет

########################## цикл с условием

value = 10
while value >= 0:
    print(value)
    value -= 1

## не очень хорошее решение
while True:
    print(value)
    value -= 1
    if value < 0:
        break

# решение под конкретную ситуацию
do_while = True
while do_while:
    print(value)
    value -= 1
    if value < 0:
        do_while = False


############################### методы строк

my_str = "qwerty"
index = 0
index = -1  # отсчет от конца строки
symbol = my_str[index]  # получение значения по индексу
print(symbol)

if index < len(my_str):
    symbol = my_str[index]  # получение значения по индексу
    print(symbol)

symbol_count = len(my_str)
print(symbol_count)

my_str[0] = "Q"  # TypeError: 'str' object does not support item assignment

#   Срезы строк
my_str = "qwerty"
new_str = my_str[1:5]  # от - включено, до - исключено
new_str = my_str[3:]  # от .. и до конца
new_str = my_str[:-3]  # от начала и до ...
new_str = my_str[:]
new_str = my_str[-40:20]
print(new_str)

new_str = "Q" + my_str[1:]
new_str = my_str[:3] + "R" + my_str[4:]
print(new_str)

new_str = my_str[::2]  # 2 - шаг среза. Значения на четных индексах
new_str = my_str[1::2]  # 2 - шаг среза. Значения на нечетных индексах
new_str = my_str[::-1]  # разворот строки
print(new_str)

my_str = 'asD'
if my_str[-1].isupper():  # метод строки
    print("This is number", my_str)
