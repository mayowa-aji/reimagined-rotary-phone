#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return 'Welcome to the Pizza Shop'

@app.route('/restaurants', methods=['GET'])
def restaurants():
   restaurant_list = [restaurant.to_dict() for restaurant in Restaurant.query.all()]

   if request.method == 'GET':
       response = make_response(
           jsonify(restaurant_list),
           200
       )

       return response




@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()

    if not restaurant:
        response_dict = {
         "error": "Restaurant not found"
        }

        response = make_response(
            jsonify(response_dict),
            404
        )
        return response

    elif request.method == 'GET':
        response = make_response(
            jsonify(restaurant.to_dict()),
            200
        )
        return response

    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()

        response = {'', 200}

        return response



@app.route('/pizzas', methods = ['GET'])
def pizzas():
    pizza_list = [pizza.to_dict() for pizza in Pizza.query.all()]

    if request.method == 'GET':
        response = make_response(
            jsonify(pizza_list),
            200
        )
        return response




@app.route('/restaurant_pizzas', methods=['POST'])
def restaurant_pizzas():

    request_json = request.get_json()
    new_pizza= Pizza(
        price = request_json.get('price'),
        pizza_id = request_json.get('pizza_id'),
        restaurant_id= request_json.get('restaurant_id')
    )
    db.session.add(new_pizza)
    db.session.commit()

    if not new_pizza:
        response_dict = {"errors": ["validation errors"]}
        response = make_response(response_dict.to_dict(),500)

    else:
        response = make_response(new_pizza.to_dict())
        return response


if __name__ == '__main__':
    app.run(port=5555)
