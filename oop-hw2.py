class Device:
    def __init__(self, name, brand, model, power, price, color, isOn ):
        self.name = name
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price
        self.color = color
        self.isOn = isOn

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def __str__(self):
        return (f"Назва: {self.name}\n"
                f"Виробник: {self.brand}\n"
                f"Модель: {self.model}\n"
                f"Потужність: {self.power} Вт\n"
                f"Ціна: {self.price} грн\n"
                f"Колір: {self.color}\n"
                f"Стан: {'Увімкнений' if self.isOn else 'Вимкнений'}")

    def set_power(self, power):
        if isinstance(power, int) and power > 0  :
            self.power = power
        return

    def set_price(self, price):
        if isinstance(price, int) and price > 0  :
            self.price = price
        return

class CoffeeMachine(Device):
    def make_coffee(self):
        if self.isOn:
            print("Кава готується")
        else:
            print("Кавомашина вимкнена")

class Blender(Device):
    def blend(self):
        if self.isOn:
            print("Подрібнюємо продукти")
        else:
            print("Блендер вимкнений")

class MeatGrinder(Device):
    def grind_meat(self):
        if self.isOn:
            print("Подрібнюємо м'ясо")
        else:
            print("М'ясорубка вимкнена")


class Ship:
    def __init__(self, name, country, displacement, length, speed, year_built, is_sailing):
        self.name = name
        self.country = country
        self.displacement = displacement
        self.length = length
        self.speed = speed
        self.year_built = year_built
        self.is_sailing = is_sailing

    def __str__(self):
        return (f"Назва: {self.name}\n"
                f"Країна: {self.country}\n"
                f"Водотоннажність: {self.displacement} тонн\n"
                f"Довжина: {self.length} м\n"
                f"Максимальна швидкість: {self.speed} вузлів\n"
                f"Рік побудови: {self.year_built}\n"
                f"Стан: {'У русі' if self.is_sailing else 'Стоїть'}")

    def start_sailing(self):
        self.is_sailing = True

    def stop_sailing(self):
        self.is_sailing = False

class Frigate(Ship):
    def patrol(self):
        if self.is_sailing:
            print("Фрегат патрулює морську територію.")
        else:
            print("Фрегат стоїть у порту.")

class Destroyer(Ship):
    def detect_threats(self):
        if self.is_sailing:
            print("Есмінець виявляє загрози.")
        else:
            print("Есмінець стоїть у порту.")

class Cruiser(Ship):
    def manage_mission(self):
        if self.is_sailing:
            print("Крейсер виконує бойове завдання.")
        else:
            print("Крейсер стоїть у порту.")



class Money:
    def __new__(cls,currency, money, coins):
        if money < 0 or coins < 0 or coins > 99:
            raise ValueError("Money must be between 0 and 99")
        return super().__new__(cls)

    def __init__(self, currency, money, coins):
        self.currency = currency
        self.money = money
        self.coins = coins

    def __str__(self):
        return f"      {self.money}.{self.coins} {self.currency}"

    def input_money(self):
        self.currency = input("введіть валюту:")
        self.money = int(input("введіть цілу частину:"))
        self.coins = int(input("введіть копійки:"))


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f" {self.name} - {self.price}"


    def __sub__(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Зменшення ціни має бути невід'ємним числом")

        total = self.price.money * 100 + self.price.coins
        discount = round(amount * 100)
        new_total = total - discount

        if new_total < 0:
            raise ValueError("Ціна не може бути від'ємною")

        new_money = Money(
            self.price.currency,
            new_total // 100,
            new_total % 100
        )

        return Product(self.name, new_money)


money = Money("грн", 45, 50)

milk = Product("Молоко", money)

print("Початкова ціна:")
print(milk)

milk = milk - 10

print("\nЦіна після зменшення на 10 грн:")
print(milk)

milk = milk - 5.50

print("\nЦіна після зменшення ще на 5.50 грн:")
print(milk)

coffee_machine = CoffeeMachine(
    "Кавомашина", "DeLonghi", "ECAM22",
    1450, 12000, "Чорний", True
)

blender = Blender(
    "Блендер", "Bosch", "MSM",
    800, 2500, "Білий", False
)

meat_grinder = MeatGrinder(
    "М'ясорубка", "Moulinex", "ME306",
    1600, 4000, "Сірий", True
)

print(coffee_machine)
coffee_machine.make_coffee()

print("\n", blender, end=" ")
blender.blend()
blender.turn_on()
blender.blend()

print("\n", meat_grinder, end=" ")
meat_grinder.grind_meat()
meat_grinder.turn_off()
meat_grinder.grind_meat()

print("\n =================================== \n")

frigate = Frigate(
    "Гетьман Сагайдачний", "Україна",
    3500, 123, 30, 1993, True
)

destroyer = Destroyer(
    "Arleigh Burke", "США",
    9000, 155, 30, 2018, False
)

cruiser = Cruiser(
    "Крейсер", "США",
    10000, 180, 32, 2020, True
)

print(frigate)
frigate.patrol()

print("\n", destroyer, end=" ")
destroyer.detect_threats()
destroyer.start_sailing()
destroyer.detect_threats()

print("\n", cruiser, end=" ")
cruiser.manage_mission()
cruiser.stop_sailing()
cruiser.manage_mission()

