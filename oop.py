class Counter:
    counter = 0
    def __init__(self):
        self.counter += 1

a = Counter()
b = Counter()
print(a.counter)
print(b.counter)


class User:
    test_counter=0
    __counter = 0
    def __init__(self, name, age):
        User.counter += 1
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age >= 120:
            raise ValueError(f"Invalid Age {new_age}")
        self.__age = new_age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def show(self):
        return f'{self.name} is {self.age} years old'

    @staticmethod
    def get_counter():
        return User.counter

user1 = User('John', 18)
print(user1.show())
print(user1)
# __new__
#__init__
user = User.__new__(User)

User.test_counter += 1


print(User.counter)

class Person:
    def __init__(self, name, surname, birthday, phone, city, country, address):
        self.__name = name
        self.__surname = surname
        self.__birthday = birthday
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError(f"Invalid name {new_name}")
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if new_surname is None or new_surname == "":
            raise ValueError(f"Invalid surname {new_surname}")
        self.__surname = new_surname

    def __str__(self):
        return (
            f" {self.__name} {self.__surname}\n"
            f"Дата народження: {self.__birthday}\n"
            f"Телефон: {self.__phone}\n"
            f"Місто: {self.__city}\n"
            f"Країна: {self.__country}\n"
            f"Домашня адреса: {self.__address}"
        )



    def inputUser(self):
        self.__name = input("Введіть ім'я: ")
        self.__surname = input("Введіть прізвище: ")
        self.__birthday = input("Введіть дату народження: ")
        self.__phone = input("Введіть контактний телефон: ")
        self.__city = input("Введіть місто: ")
        self.__country = input("Введіть країну: ")
        self.__address = input("Введіть домашню адресу: ")


person4 = Person("Іван", "Петренко", "15.05.2000",
                "+380501234567", "Ужгород",
                "Україна", "вул. Шевченка, 10")

try:
    print(person4.name)
    print(person4.surname)

    person4.name = "Олександр"
    person4.surname = "Коваленко"

    print(person4.name)
    print(person4.surname)

    person4.name = ""
    person4.surname = ""

    print(person4.name)
    print(person4.surname)
except ValueError as e:
    print(e)

person = Person("Іван","Іваненко","15.10.2000","+380991234567","Черкаси","Україна","вул. Шевченка, 14")

print(person)

person2 = Person.__new__(Person)

person2.inputUser()

print(person2)

try:
    user2 = User("Bob", 18)
    print(user2)
    user2.age += 1
    print(user2)
    user2.age = 140
    print(user2)
except ValueError as e:
    print(e)

print(User.get_counter())