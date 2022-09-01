# тип bool, None
# приведение типов
# оператор if

##################################################################

my_strange_value = None
print(my_strange_value, type(my_strange_value))

value_1 = 3
value_2 = 4
result = print(value_1 + value_2)
print(result)

##################################################################

# my_bool_value = False
# print(my_bool_value, type(my_bool_value))

# my_bool_value = 10 == 2
## <, >, <=, >=, ==, !=
## not
# new_value = not my_bool_value
# print(my_bool_value, new_value)

value_1 = True
value_2 = True
result = value_1 and value_2  # логическое И - муж пьет чай, а жена кофе

print(result)

value_1 = False
value_2 = False
result = value_1 or value_2  # логическое ИЛИ - Я пью чай или кофе

print(result)

number = 6
color = "red"

result = (number >= 5 or
          not number == 1 and
          color == 'red')

print(result)

#################################

value = 123

if value > 100:
    print(f"Value more than 100")
else:
    print(f"Value less or equal than 100")

# if условие:
#     # блок, если ДА
# elif условие_2:
#     # блок, если ДА
#  ...................
# else:
#     # блок, если НЕТ

value = 0
if value > 0:
    print(f"Value is positive number")
elif value < 0:
    print(f"Value is negative number")
else:
    print(f"Value is 0")

#####################################################
# приведение типов

value_int = 10
value_float = float(value_int)
print(value_float, type(value_float), value_int, type(value_int))

value = 10
value = float(value)
print(value, type(value))

value = -10.9
value = int(value)
print(value, type(value))

value = -10
value = str(value)
print(value, type(value))

value = "100_0_00"
value = int(value)
print(value, type(value))

value = "-100.078"
value = float(value)
print(value, type(value))

value = None
value = str(value)
print(value, type(value))

value = -10   # int -> bool True, кроме 0
value = bool(value)
print(value, type(value))

value = 0.0000000000000001   # float -> bool True, кроме 0.0
value = bool(value)
print(value, type(value))

value = ""   # str -> bool True, кроме ""     !!!!!!!
value = bool(value)
print(value, type(value))

value = None   # None -> bool всегда False     !!!!!!!
value = bool(value)
print(value, type(value))

my_str = "qwerty"
number = 123
my_value = str(number)
print(my_value, type(my_value))


value = None

if not value:
    print("Value is None")

if value:
    print(f"This value {value} is not 0")

#####################################################
## in

my_str = "<SJHDGfj<SHVMGXJzxcvJSDCHALSJhjSGVC"
sub_str = 'zxc'

if sub_str in my_str:
    print("!!!!!!!!!!!!!")


value_1 = 19
value_2 = 2

if value_1 % 2 == 0:
    if value_2 > 0:
        print("Case 1")
    else:
        print("Case 2")
else:
    print("Case 3")

#####################################################
value_1 = 11

if value_1 % 2 == 0 and value_1 % 3 == 0:
    print("Делится на 6")
elif value_1 % 2 == 0:
    print("Делится на 2")
elif value_1 % 3 == 0:
    print("Делится на 3")
else:
    print("Не делится ни на 2 ни на 3")
#####################################################
if value_1 % 2 == 0:
    print("Делится на 2")
else:
    print("НЕ Делится на 2")
if value_1 % 3 == 0:
    print("Делится на 3")
else:
    print("Не делится на 3")