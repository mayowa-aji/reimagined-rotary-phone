from flask_sqlalchemy import SQLAlchemy
from flask_serialize import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)