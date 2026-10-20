class MyMeta(type):
    # mcsl - посилвння на наш клас
    # name - назва
    # bases - tuple (батьківські класи)
    # attrs - dict {name : "Alex", say_hi : lambda self: f'hello, self.name.'}
    def __new__(mcls, name, bases, attrs):
        print(f'Створився клас {name}')
        attrs['category'] = 'general'
        return super().__new__(mcls, name, bases, attrs)

class Product(metaclass=MyMeta):
    pass

class User(metaclass=MyMeta):
    pass

# p = Product()
# print(p.category)