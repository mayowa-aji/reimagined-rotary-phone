#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return ''

@app.route('/restaurants')
def restaurants():
    return ''

@app.route('/restaurants/<int:id>')
def restaurant_by_id(id):
    return ''

@app.route('/pizzas')
def pizzas():
    return ''

@app.route('/restaurant_pizzas')
def resaurant_pizzas():
    return ''


if __name__ == '__main__':
    app.run(port=5555)
