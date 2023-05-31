from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def show_orders():
    return render_template("index.html", order_list = orders)

@app.route('/orders/<1>')
def show_one_order():
    return render_template("index.html", )