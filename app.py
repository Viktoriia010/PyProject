#FLASK -  мінімалістичний фреймворк

from flask import Flask, render_template
from unicodedata import category

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def home():
    menu = ['Home', 'about', 'contact']
    return render_template('index.html', title='Home', menu=menu)

@app.route('/fruits')
def fruits():
    menu2 = [ 'Головна', 'Каталог', 'Про нас', 'Доставка', 'Контакти']
    categories = [
        {
            "name": "🍏 Всі фрукти",
            "count": 24
        },
        {
            "name": "🍒 Ягоди",
            "count": 6
        },
        {
            "name": "🍊 Цитрусові",
            "count": 5
        },
        {
            "name": "🍑 Кісточкові",
            "count": 4
        },
        {
            "name": "🥭 Тропічні",
            "count": 5
        },
        {
            "name": "🍎 Яблука та груші",
            "count": 4
        }
    ]
    return render_template('fruits.html', title='Fruits', menu2=menu2, categories=categories)

if __name__ == '__main__':
    app.run(debug=True) # в продакшн має бути false