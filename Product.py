import uuid


class Product:
    def __init__(self,title, price, rating, reviews, image):
        self.id = uuid.uuid4()
        self.title = title
        self.price = price
        self.image = image
        self.rating = rating
        self.reviews = reviews

