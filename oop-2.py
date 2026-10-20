from Student import StudentOnline
from abc import ABC, abstractmethod
# def __init__(self, name, age):
    #     super().__init__(name, age)

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Car moved")

class Bus(Transport):
    def move(self):
        print("Bus moved")

def drive(transport):
    if isinstance(transport, Transport):
        transport.move()


class Printer:
    def __init__(self, model):
        self.model = model

    def print_doc(self, document):
        if isinstance(document, Document):
            print(f"принтер: {self.model}")
            document.print_doc()

class Document(ABC):
    def __init__(self, title, text, ext, pages):
        self.title = title
        self.text = text
        self.ext = ext
        self.pages = pages

    @abstractmethod
    def print_doc(self):
        pass

class ExcellDocument(Document):
    def print_doc(self):
        print(f"    Excel-документ: {self.title}")
        print(f"текст: {self.text}")
        print(f"формат: {self.ext}")
        print(f"ст: {self.pages}")

class WordDocument(Document):
    def print_doc(self):
        print(f"    Word-документ: {self.title}")
        print(f"текст: {self.text}")
        print(f"формат: {self.ext}")
        print(f"ст: {self.pages}")

class HtmlDocument(Document):
    def print_doc(self):
        print(f"   HTML-документ: {self.title}")
        print(f"текст: {self.text}")
        print(f"формат: {self.ext}")
        print(f"ст: {self.pages}")




printer = Printer("Canon")

excel = ExcellDocument("Таблиця", "Оцінки студентів", ".xlsx", 4)

word = WordDocument("Резюме", "Інформація про мене", ".docx", 3)

html = HtmlDocument("Сайт", "Моя вебсторінка", ".html", 1)

printer.print_doc(excel)
print()

printer.print_doc(word)
print()

printer.print_doc(html)


# tr=Car()
# tr.move()

# s = StudentOnline.from_string("Ivan:20")
# print(type(s))

# s = Student.from_string("Ivan:20")
# print(s)

    # my_tuple = (1, 2, 3) #кортеж
    # print(my_tuple)


