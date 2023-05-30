from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    product_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))

class Location(db.Model):
    location_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))

class ProductMovement(db.Model):
    movement_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime)
    from_location = db.Column(db.String(50), db.ForeignKey('location.location_id'))
    to_location = db.Column(db.String(50), db.ForeignKey('location.location_id'))
    product_id = db.Column(db.String(50), db.ForeignKey('product.product_id'))
    qty = db.Column(db.Integer)

@app.route('/')
def index():
    return 'Welcome to the Inventory Management App'

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        product_id = request.form['product_id']
        name = request.form['name']
        product = Product(product_id=product_id, name=name)
        db.session.add(product)
        db.session.commit()
        return redirect('/products')
    else:
        products = Product.query.all()
        return render_template('products.html', products=products)

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    if request.method == 'POST':
        location_id = request.form['location_id']
        name = request.form['name']
        location = Location(location_id=location_id, name=name)
        db.session.add(location)
        db.session.commit()
        return redirect('/locations')
    else:
        locations = Location.query.all()
        return render_template('locations.html', locations=locations)

@app.route('/movements', methods=['GET', 'POST'])
def movements():
    if request.method == 'POST':
        movement_id = request.form['movement_id']
        timestamp = request.form['timestamp']
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        product_id = request.form['product_id']
        qty = request.form['qty']
        movement = ProductMovement(movement_id=movement_id, timestamp=timestamp,
                                   from_location=from_location, to_location=to_location,
                                   product_id=product_id, qty=qty)
        db.session.add(movement)
        db.session.commit()
        return redirect('/movements')
    else:
        movements = ProductMovement.query.all()
        return render_template('movements.html', movements=movements)

if __name__ == '__main__':
    app.run(debug=True)
