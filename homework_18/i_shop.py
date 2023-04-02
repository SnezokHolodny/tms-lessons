import sqlite3
from dataclasses import dataclass
from flask import Flask, session, abort, redirect, request
from flask_session import Session


DATABASE_FILE = 'i_shop.db'
@dataclass
class Product:
    id: int
    name: str
    discription: str
    category: str

def load_products() -> list[Product]:
    storage = []
    with sqlite3.connect("i_shop.db") as connection:
        full_list = connection.execute("Select id, name ,discription,category from product")
        for i in full_list.fetchall():
            element = Product(*i)
            storage.append(element)
        return storage


def information_of_produtc(product_id: int) -> Product:
    with sqlite3.connect("i_shop.db") as connection:
        result = connection.execute("Select id, name, discription, category from product where id=?", (product_id,))
        rows = result.fetchall()
        if len(rows) != 1:
            raise ValueError(f"This id not found {product_id}")
        return Product(*rows[0])


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@app.route('/products')
def all_products():
    products = load_products()
    products_html = "\n".join(f"<li><a href='/product/{product.id}'>{product.name}</li>" for product in products)
    return f"""
    <html>
        <head>
            <title> Product shop </title>
        </head>
        <body>
            <a href="/product_list">Favorite products</a>
            <h1> Product List </h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    """


@app.route('/product/<int:product_id>')
def list_of_product(product_id: int):
    try:
        product = information_of_produtc(product_id)
    except ValueError as e:
        abort(404, e)
    star=""
    favarite_products=session.get('favorite_products', set())
    if product.id in favarite_products :
        star="&#9989"
    return f'''
    <html>
        <head>
            <title> {product.name} </title>
        </head>
        <body>
            <a href="/products"> Main page</a>
            <h1> Name:{product.name} {star} </h1>
            <h2> Description:{product.discription} </h2>
            <h3> Category:{product.category} </h3>
            <h3> {count_favorites_products}
            <form method="post" action="/product/favorites_products">
                <input type="hidden" name="products_id" value="{product.id}"/>
                <input type="submit" value="Add favorites products "/>
            </form>
        </body>
    </html>
    '''

@app.route("/product/favorites_products", methods=["POST"])
def count_favorites_products():
    product_id = int(request.form["products_id"])
    product = information_of_produtc(product_id)
    favorite_products = session.setdefault('favorite_products', set())
    if product.id in favorite_products:
        favorite_products.remove(product.id)

    else:
        favorite_products.add(product.id)
    return redirect(f'/product/{product.id}')

@app.route("/product_list")
def generate_html_list():
    basket_list=[]
    favorite_product=session.get('favorite_products', set())
    for i in favorite_product:
        basket_list.append(information_of_produtc(i))
    products_html = "\n".join(f"<li><a href='/product/{product.id}'>{product.name}</li>" for product in basket_list)
    return f"""
    <html>
        <head>
            <title> Favorite Products </title>
        </head
        <body>
            <h1> Favorite Products: </h1>
            <ul>
                {products_html}
            </ul>
        </body>
    </html>
    """






print(load_products())
print(information_of_produtc(1))
if __name__ == '__main__':
    app.run(port=8080, debug=True)