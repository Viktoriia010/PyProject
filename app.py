#FLASK -  мінімалістичний фреймворк

from flask import Flask, render_template, request
from unicodedata import category

from Product import Product
from models.ProductModel import ProductModel, method

app = Flask(__name__)

# params, query params
# http://localhost:5000/product/23
# http://localhost:5000/product?id=23

products = ['bread', 'milk', 'tomato', 'eggs']

@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    title = data['title']
    products.append(title)
    return {
        'title': title,
    }, 201

@app.route('/product/<int:id>')
def product(id):
    return f'You have {id} {products[id]}'
    #return render_template('product.html', id=id)


@app.route('/product/<title>')
def product_by_title(title):
    return f'You have {title}'
    #return render_template('product.html', id=id)


@app.route('/product')
def product_by_id():
    print(request.args.get('title'))
    id = int(request.args.get('id'))
    # return f'You have product {id}'
    return render_template('product.html', id=id)





@app.route('/index')
@app.route('/')
def home():
    menu = ['Home', 'about', 'contact']
    return render_template('index.html', title='Home', menu=menu)



menu2 = ['Головна', 'Каталог', 'Про нас', 'Доставка', 'Контакти']


@app.route('/fruits')
def fruits():
    categories = [
        {
            "name": "🍏 Всі фрукти",
            "data-category": "all",
            "count": 24
        },
        {
            "name": "🍒 Ягоди",
            "data-category": "berries",
            "count": 6
        },
        {
            "name": "🍊 Цитрусові",
            "data-category": "citrus",
            "count": 5
        },
        {
            "name": "🍑 Кісточкові",
            "data-category": "stone-fruits",
            "count": 4
        },
        {
            "name": "🥭 Тропічні",
            "data-category": "tropical",
            "count": 5
        },
        {
            "name": "🍎 Яблука та груші",
            "data-category": "apples",
            "count": 4
        }
    ]
    fruits = method.get_all_products()
    return render_template('fruits.html', title='Fruits', menu2=menu2, categories=categories, products=fruits)

@app.route('/fruit/<uuid:id>')
def fruit(id):
    product = method.get_product_by_id(id)
    return render_template('fruit.html', title='Fruit', menu2=menu2,  product=product)

@app.route('/add-fruit', methods=['POST'])
def create_fruit():
    data = request.form
    title = data['title']
    price = float(data['price'])
    rating = float(data['rating'])
    reviews = int(data['reviews'])
    image = data['image']
    p = Product(title, price, rating, reviews, image)
    method.create_product(p)
    return {
        'message': 'продукт додано успішно'
    }, 201


@app.route('/add-fruit')
def create_fruit_page():
    fruits = method.get_all_products()
    return render_template('fruit-form.html', title='Create fruit', products=fruits)


if __name__ == '__main__':
    app.run(debug=True) # в продакшн має бути false