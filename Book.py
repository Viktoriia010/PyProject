class Book:
    def __new__(cls, title, author, year, pages):
        if not isinstance(year, int) or year < 0 or year > 2026:
                raise ValueError("Year must be between 0 and 2026")
        if not isinstance(pages, int) or pages < 0:
                raise ValueError("Pages must be greater than 0")
        return super().__new__(cls)

    def __init__(self, title, author, year , pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages



    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year}, {self.pages} pages"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, word):
        return word.lower() in self.title.lower()

    def __bool__(self):
        return bool(self.title) and bool(self.author) and self.pages > 0


