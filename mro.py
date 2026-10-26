
class A3:
    def __init__(self):
        print("Init A3")
        super().__init__()


class B3:
    def __init__(self):
        print("Init B3")
        super().__init__()

class A2(A3):
    def __init__(self):
        print("Init A2")
        super().__init__()


class B2:
    def __init__(self):
        print("Init B2")
        super().__init__()


class A1(A2):
    def __init__(self):
        print("Init A1")
        super().__init__()


class B1:
    def __init__(self):
        print("Init B1")
        super().__init__()

class A(A1):
    def __init__(self):
        print("Init A")
        super().__init__()


class B:
    def __init__(self):
        print("Init B")
        super().__init__()



class C(A,B):
    def __init__(self):
        print("Init C")
        super().__init__()

# print(C.mro())
#
# print(C.__mro__)

c = C()