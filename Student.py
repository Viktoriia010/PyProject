
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test1(self):
        print(self)
        print("test1")

    @classmethod
    def from_string(cls, serialize_object): #"Ivan:20"
        obj = serialize_object.split(":")
        return cls(obj[0], obj[1])


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    @staticmethod
    def test3():
        pass
    pass


class StudentOnline(Student):
    pass