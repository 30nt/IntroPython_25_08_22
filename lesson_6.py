# кортежи и списки

my_tuple = (1, 2, 3, "qwe", True, ("a", "b"), None, [])  # неизменяемы тип
# print(type(my_tuple), my_tuple)

my_list = [1, 2, 3, "qwe", True, ("a", "b"), None, []]  # изменяемы тип
# print(type(my_list), my_list)

########################

my_tuple[-1].append(1)
my_tuple[-1].extend([2, 3.14])
my_tuple[-1].pop()
print(my_tuple)

########################

my_list = []
new_list = [my_list.copy()] * 3
print(new_list)

my_list.append(1)
print(new_list, my_list)

# new_list[0].append(2)    # TODO
# print(new_list)

######################
my_list[0] = 100
print(my_list)

my_tuple[0] = 100  # TypeError
print(my_tuple)

new_values = tuple(my_list)
new_values = list(my_tuple)
print(new_values, type(new_values))

new_values = list(my_tuple)
new_values[0] = 100
my_tuple = tuple(new_values)
print(my_tuple)

########################
new_list = []
# new_list = list()
# print(new_list)

for number in range(1, 11):
    new_list.append(number)

new_list.append("qwe")  # O(1)
new_list.insert(0, "asd")  # O(n)
print(new_list)

value = new_list.pop()  # O(1)
new_list.pop(0)  # O(n)
print(value, new_list)

## возврат значения   - pop возвращает удаленное значение
#######################

# result = my_list[:2] + my_list[5:]
# print(result)

# items_1 = [1, 2, 3, "a"]
# items_2 = ["q", "w", "e"]
#
# result = []
# print(result, id(result))
#
# result = items_1 + items_2  # меняет id
#
# result.extend(items_1)  # не меняет id
# result.extend(items_2)
# print(result, id(result))
#
# result += items_1  # не меняет id
# result += items_2
# print(result, id(result))
########################
#
# message = "My name is   \t   Volodymyr"
# words = message.split()
# print(words)
#
# ip_address = "127.255.12.0"
# groups = ip_address.split(".")
# print(groups)
#
# filename = "/home/volodymyr/PycharmProjects/IntroPython_25_08_22/"
# path = filename.strip("/").split("/")
# print(path)
#
# new_message = " ".join(words)
# print(new_message)
#
# new_filename = "C:\\\\" + "\\".join(path)
#
# print(new_filename)

########################
# print(len(my_list), len(my_tuple))

# index = 5
# value = my_tuple[-1]
# value = my_list[index]
# print(value)

# start = 1
# finish = 3
# values = my_list[start:finish]
# values = my_tuple[::-1]
# print(values)

# for value in my_list[::-1]:
#     print(value)