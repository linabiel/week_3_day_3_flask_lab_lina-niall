from flask import render_template
from app import app
from models.order_list import orders_list

@app.route('/orders')
def orders():
    return render_template('orders.html', orders_list=orders_list)

@app.route('/orders/<index>')
def order(index):
    sample_order = orders_list[int(index)]
    return render_template('order.html', order=sample_order)