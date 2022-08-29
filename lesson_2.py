# print(1+2)
# Ctrl + ? (Mac: Command + ?)

value_1 = 4  # int
value_1 *= 2  #  value_1 = value_1 * 2
print(f"{value_1=}")
value_2 = 0.5  # float
result = value_1 * value_2
result = value_1 / value_2
result = value_1 // value_2  # целочисленное деление
result = value_1 % value_2   # остаток от деления
result = value_1 ** value_2
print(result)


################## однобуквенные названия ТОЛЬКО для математических объектов!!!
# a = 2
# b = 3
# c = 4
# D = b ** 2 - 4 * a * c

# PEP-8 formatting Alt+Ctrl+L (Mac Option+Command+L)

active_users_count = 1000
price = 10

total_money = active_users_count * price

# PascalCaseObjectNotification
# camelCaseObjectNotification
# cebab-object-notification

RATIO = 100
print(total_money, RATIO)

value_type = type(value_2)
print(value_2, value_type)

value = 123123123
new_value = 123123123
print(id(value), id(new_value))

value = "qQwWe"
my_str = "zxc"
print(value, type(value))

result = value + "__" + value  # конкатенация
# result = value - my_str

result = ("123" + "5") * 2
print(result)

################### Литералы строк ##################

my_str = "New_string"
my_str = 'New_string'
my_str = """New_string"""
my_str = '''New_string'''

my_str = 'FC "Arsenal"'
my_str = "I'm a boy"

my_str = 'My\tname\'is\nVova'
new_str = r'My\tname\tis\nVova'  # raw string
format_str = f"{value=}"
print(my_str)
print(new_str)
print(format_str)







