from Product import Product


class ProductModel:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def create_product(self, product:Product):
        self.products.append(product)
        return product



products = [
    Product("Банани", 45, 4.8, 124,
            "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=600&q=85"),

    Product("Яблука", 35, 4.7, 98,
            "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=85"),

    Product("Апельсини", 55, 4.9, 156,
            "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=600&q=85"),

    Product("Полуниця", 120, 4.8, 87,
            "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=600&q=85"),

    Product("Чорниця", 150, 4.9, 72,
            "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=600&q=85"),

    Product("Виноград", 95, 4.6, 64,
            "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=600&q=85"),

    Product("Ківі", 80, 4.7, 63,
            "https://images.unsplash.com/photo-1585059895524-72359e06133a?auto=format&fit=crop&w=600&q=85"),

    Product("Манго", 140, 4.8, 45,
            "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=600&q=85")
]

method = ProductModel(products)