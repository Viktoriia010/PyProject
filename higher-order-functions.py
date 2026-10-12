import time


def print_horizontally(symbol):
    for i in range(1,11):
        print(symbol, end="")
    print()

def print_vertically(symbol):
    for i in range(1,11):
        print(symbol)


def show_line(symbol, function_to_call):
    return function_to_call(symbol)


while True:
    print("1 - горизонтально ")
    print("2 - вертикально ")
    print("0 - вийти")

    choice = input("вибір: ")

    symbol = input("символ: ")

    if choice == "1":
        show_line(symbol, print_horizontally)

    elif choice == "2":
        show_line(symbol, print_vertically)

    elif choice == "0":
        break



def measure_time(func):
    def wrapper(num):
        start = time.time()
        res = func(num)
        end = time.time()
        print(f"Час виконання функції: {end - start:.3f} секунд")
        print("Сума чисел:", res)
    return wrapper

@measure_time
def calculate_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

calculate_sum(1000000)