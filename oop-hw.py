# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску,
# виробника, об'єм двигуна, колір машини, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Car:
    def __init__(self, name, manufacture,manufacturer, engine_capacity, price, color, ):
        self.__name = name
        self.__manufacture = manufacture
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__price = price
        self.__color = color

    def __str__(self):
        return (
            f"  {self.__name} \n"
            f"рік випуску: {self.__manufacture}\n"
            f"виробник: {self.__manufacturer}\n"
            f"об'єм двигуна: {self.__engine_capacity}\n"
            f"ціна: {self.__price}\n"
            f"колір машини: {self.__color}"
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError(f"Invalid name {new_name}")
        self.__name = new_name

    @property
    def manufacture(self):
        return self.__manufacture

    @manufacture.setter
    def manufacture(self, new_manufacture):
        if new_manufacture is None or new_manufacture == "":
            raise ValueError(f"Invalid manufacture {new_manufacture}")
        self.__manufacture = new_manufacture

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        if new_manufacturer is None or new_manufacturer == "":
            raise ValueError(f"Invalid manufacture {new_manufacturer}")
        self.__manufacturer = new_manufacturer

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, new_engine_capacity):
        if new_engine_capacity < 0:
            raise ValueError(f"Invalid engine capacity {new_engine_capacity}")
        self.__engine_capacity = new_engine_capacity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError(f"Invalid price {new_price}")
        self.__price = new_price

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if new_color is None or new_color == "":
            raise ValueError(f"Invalid color {new_color}")
        self.__color = new_color


    def input_car(self):
        self.__name = input("Введіть назву моделі: ")
        self.__manufacture = int(input("Введіть рік випуску: "))
        self.__manufacturer = input("Введіть виробника: ")
        self.__engine_capacity = float(input("Введіть об'єм двигуна: "))
        self.__price = float(input("Введіть ціну: "))
        self.__color = input("Введіть колір машини: ")


car = Car("Civic", "2022", "Honda", 1.5, 800000, "чорний")

print(car)
print(car.price)

car.price = 750000
car.color = "білий"

print(car)



# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __str__(self):
        return (
            f"Назва книги: {self.__name}\n"
            f"Рік видання: {self.__year}\n"
            f"Видавець: {self.__publisher}\n"
            f"Жанр: {self.__genre}\n"
            f"Автор: {self.__author}\n"
            f"Ціна: {self.__price}"
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError(f"Invalid name {new_name}")
        self.__name = new_name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 0:
            raise ValueError(f"Invalid year {new_year}")
        self.__year = new_year

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher):
        if new_publisher is None or new_publisher == "":
            raise ValueError(f"Invalid publisher {new_publisher}")
        self.__publisher = new_publisher

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, new_genre):
        if new_genre is None or new_genre == "":
            raise ValueError(f"Invalid genre {new_genre}")
        self.__genre = new_genre

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if new_author is None or new_author == "":
            raise ValueError(f"Invalid author {new_author}")
        self.__author = new_author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError(f"Invalid price {new_price}")
        self.__price = new_price

    def input_book(self):
        self.__name = input("Введіть назву книги: ")
        self.__year = int(input("Введіть рік видання: "))
        self.__publisher = input("Введіть видавця: ")
        self.__genre = input("Введіть жанр: ")
        self.__author = input("Введіть автора: ")
        self.__price = float(input("Введіть ціну: "))


book = Book("Кобзар", 1840, "Друкарня", "Поезія", "Тарас Шевченко", 300)

print(book)
print(book.price)

book.price = 350
book.genre = "Класична література"

print(book)

# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __str__(self):
        return (
            f"Назва стадіону: {self.__name}\n"
            f"Дата відкриття: {self.__opening_date}\n"
            f"Країна: {self.__country}\n"
            f"Місто: {self.__city}\n"
            f"Місткість: {self.__capacity} осіб"
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name is None or new_name == "":
            raise ValueError(f"Invalid name {new_name}")
        self.__name = new_name

    @property
    def opening_date(self):
        return self.__opening_date

    @opening_date.setter
    def opening_date(self, new_opening_date):
        if new_opening_date is None or new_opening_date == "":
            raise ValueError(f"Invalid opening date {new_opening_date}")
        self.__opening_date = new_opening_date

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        if new_country is None or new_country == "":
            raise ValueError(f"Invalid country {new_country}")
        self.__country = new_country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        if new_city is None or new_city == "":
            raise ValueError(f"Invalid city {new_city}")
        self.__city = new_city

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity < 0:
            raise ValueError(f"Invalid capacity {new_capacity}")
        self.__capacity = new_capacity

    def input_stadium(self):
        self.__name = input("Введіть назву стадіону: ")
        self.__opening_date = input("Введіть дату відкриття: ")
        self.__country = input("Введіть країну: ")
        self.__city = input("Введіть місто: ")
        self.__capacity = int(input("Введіть місткість стадіону: "))

stadium = Stadium("Олімпійський", "12.08.1923", "Україна", "Київ", 70050)

print(stadium)
print(stadium.capacity)

stadium.capacity = 80000
stadium.city = "Львів"

print(stadium)