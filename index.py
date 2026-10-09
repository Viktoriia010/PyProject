def odd_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i  #виводить значення по одному


for num in odd_numbers(1, 10):  # кожен раз при наступній ітерації у функції буде проситись наступне значення
    print(num)

for num in odd_numbers(11, 1):  # звичайну функцію так не можна викликати, тільки якщо вона є генератором
    print(num)

print(20*"*")

#==============================================================


def multiple_of_five(a, b):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if i % 5 == 0:
            yield i  #виводить значення по одному


for num in multiple_of_five(1, 30):  # кожен раз при наступній ітерації у функції буде проситись наступне значення
    print(num)

for num in multiple_of_five(36, 1):  # звичайну функцію так не можна викликати, тільки якщо вона є генератором
    print(num)


print(20*"*")

#==============================================================

def palindromes(a, b):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            yield i  #виводить значення по одному


for num in palindromes(1, 200):  # кожен раз при наступній ітерації у функції буде проситись наступне значення
    print(num)

for num in palindromes(202, 1):  # звичайну функцію так не можна викликати, тільки якщо вона є генератором
    print(num)