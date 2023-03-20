from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }


    def __repr__(self):
        return f'<Restaurant name={self.name} address={self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    restaurant_pizzas = db.relationship('RestaurantPizza', backref = 'pizza')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f'<Pizza name={self.name} address={self.address}>'


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, db.CheckConstraint('price >=1 and price <=30'))
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    def to_dict(self):
        return{
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id
        }

    def __repr__(self):
        return f'<RestaurantPizza price={self.price}'


