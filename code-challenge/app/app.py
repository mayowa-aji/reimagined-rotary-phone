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
    return 'PIZZA APP'

@app.route('/restaurants', methods=['GET'])
def restaurants():
    restaurant_list = [restaurant.to_dict() for restaurant in Restaurant.query.all()]

    if request.method == 'GET':
        response = make_response(
            jsonify(restaurant_list),
            200
        )
        return response


@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()
    if not restaurant:
        response_dict = { "error": "Restaurant not found" }
        response = make_response(response_dict),404
        return response
        # return make_response(jsonify(
        #     {"error": "Restaurant not found"}
        # )), 404

    if request.method == 'GET':
        response = make_response(
            jsonify(restaurant.to_dict()),200
        )
        return response
        # return make_response(jsonify(restaurant.to_dict()), 200)
    elif request.method == 'DELETE':
        restaurant_pizzas= RestaurantPizza.query.filter(RestaurantPizza.restaurant_id == restaurant.id).all()

        for row in restaurant_pizzas:
            db.session.delete(row)
        db.session.delete(restaurant)
        db.session.commit()
        response = make_response(
            jsonify({''}, 200)
        )
        return response


@app.route('/pizzas', methods=['GET'])
def pizzas():
    pizza_list = [pizza.to_dict() for pizza in Pizza.query.all()]
    response = make_response(
        jsonify(pizza_list),
        200
    )
    return response

@app.route('/restaurant_pizzas', methods = ['POST'])
def resaurant_pizzas():
    request_json = request.get_json()
    new_pizza = RestaurantPizza(
        price=request_json.get('price'),
        pizza_id=request_json.get('pizza_id'),
        restaurant_id=request_json.get('restaurant_id')
    )
    db.session.add(new_pizza)
    db.session.commit()
    pizza=new_pizza.pizza
    # pizza = new_rp.pizza
    response = make_response(jsonify(pizza.to_dict()), 201)
    return response

@app.route('/pizzas/<int:id>', methods=['PATCH'])
def pizza_by_id(id):

    pizza = Pizza.query.filter(pizza.id == id).first()
    request_json = request.get_json()

    for key in request_json:
        setattr(pizza, key, request_json[key])
        db.session.add(pizza)
        db.session.commit()

        response = make_response(jsonify(pizza.to_dict()),200)
        return response


if __name__ == '__main__':
    app.run(port=5555)
