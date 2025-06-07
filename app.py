from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(500), nullable=False)  # JSON string of items
    total = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    menu_items = MenuItem.query.all()
    return render_template('index.html', menu_items=menu_items)

@app.route('/admin')
def admin():
    menu_items = MenuItem.query.all()
    return render_template('admin.html', menu_items=menu_items)

@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'category': item.category
    } for item in menu_items])

@app.route('/api/menu', methods=['POST'])
def create_menu_item():
    data = request.json
    new_item = MenuItem(
        name=data['name'],
        price=float(data['price']),
        category=data['category']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({
        'id': new_item.id,
        'name': new_item.name,
        'price': new_item.price,
        'category': new_item.category
    })

@app.route('/api/menu/<int:item_id>', methods=['PUT'])
def update_menu_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    data = request.json
    
    item.name = data['name']
    item.price = float(data['price'])
    item.category = data['category']
    
    db.session.commit()
    return jsonify({
        'id': item.id,
        'name': item.name,
        'price': item.price,
        'category': item.category
    })

@app.route('/api/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    order = Order(
        items=str(data['items']),
        total=data['total']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'success': True, 'order_id': order.id})

@app.route('/api/sales', methods=['GET'])
def get_sales():
    date = request.args.get('date')
    if date:
        orders = Order.query.filter(
            db.func.date(Order.timestamp) == date
        ).all()
    else:
        orders = Order.query.all()
    
    return jsonify([{
        'id': order.id,
        'items': order.items,
        'total': order.total,
        'timestamp': order.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for order in orders])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4036, debug=True) 