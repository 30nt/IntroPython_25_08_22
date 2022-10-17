# ООП
# класс
# атрибут класса
# экземпляр класса
# атрибут экземпляра класса
# метод экземпляра класса

class Person:  # класс
    def __init__(self, first_name: str, last_name: str, bday: str):
        self.first_name = first_name  # атрибут экземпляра класса
        self.last_name = last_name
        self.bday = bday  # атрибут экземпляра класса
        self.db_user = "user"
        self.full_name = self.get_full_name()

    def __str__(self):
        return f"name: {self.first_name}, bday: {self.bday}"

    def __repr__(self):
        return f"{self.first_name}"

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


person_1 = Person(bday="12/12/00", first_name="John", last_name="Lennon")  # экземпляр класса
person_2 = Person("Anna", "Karenina", "01/01/2000")  # экземпляр класса

# print(person_1.name, person_1.bday, person_2.name, person_2.bday)

# full_name = person_1.get_full_name(separator=" ")
# print(person_1.full_name)
# person_1.get_full_name()

print(person_1.full_name)
print(person_2)

persons = [person_1, person_2]

print(persons)


#########################################

class Person:  # класс
    # name = "John"   # атрибут класса
    name: str  # атрибут класса
    bday: str


person_1 = Person()  # экземпляр класса
person_2 = Person()  # экземпляр класса

person_2.name = "Anna"
# person_2.bday = "01/01/2000"
# person_1.bday = ""
person_1.name = "John"

print(person_1.name, person_2.name, person_2.bday, person_1.bday)
