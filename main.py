# print(__name__) #__main__
from itertools import count


def main():
    set1 = {2, 3, 4, 5, 2, 5} #унікальні значення
    set2 = {2, 3, 4, 6}
    un = set1.union(set2)
    print(un)


if __name__ == "__main__":
    main()


fruits1 = ("банан", "яблуко", "груша", "яблуко")

fruits = ("банан", "яблуко", "груша", "яблуко", "банан")
fruit = input("Введіть фрукт: ")

print("кількість", fruits.count(fruit))

fruits3 = fruits1 + fruits
print(fruits3)

cars = ["Honda", "Skoda", "BMW", "Audi", "BMW", "Mercedes", "Audi"]

name = input("Введіть назву виробника: ")
replace = input("Введіть слово для заміни: ")

for i in range(len(cars)):
    if cars[i] == name:
        cars[i] = replace

print(cars)

#======================

countries = {"Україна","Франція", "Італія", "Польща", "Німеччина"}

print("Множина країн:", countries)

while True:
    print("1 - додати")
    print("2 - видалити")
    print("3 - пошук за символами")
    print("4 - перевірити країну")
    print("5 - показати всі країни")
    print("0 - вийти")

    choice = input("вибір: ")

    if choice == "1":
        country = input("Введіть країну для додавання: ")
        countries.add(country)
        print("Країну додано")

    elif choice == "2":
        country = input("Введіть країну для видалення: ")
        countries.discard(country)
        print("Країну видалено")

    elif choice == "3":
        symbols = input("Введіть символи для пошуку: ")
        for country in countries:
            if symbols.lower() in country.lower():
                print(country)

    elif choice == "4":
        country = input("Введіть країну для перевірки: ")
        if country in countries:
            print("Країна є в множині.")
        else:
            print("Такої країни немає в множині.")

    elif choice == "5":
        print("Країни:", countries)

    elif choice == "0":
        break

    else:
        print("Неправильний вибір.")
