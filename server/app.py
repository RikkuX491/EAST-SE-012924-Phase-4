#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response, request
from flask_migrate import Migrate

### new imports start here ###
from flask_restful import Api, Resource
### new imports end here ###

from models import db, Hotel, Customer, Review

app = Flask(__name__)

# configure a database connection to the local file examples.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

### new code begins here ###
api = Api(app)
### new code ends here ###

# GET all hotels with /hotels
@app.route('/hotels', methods=['GET', 'POST'])
def all_hotels():
    if(request.method == 'GET'):
        hotels = Hotel.query.all()
        response_body = [hotel.to_dict(only=('id', 'name')) for hotel in hotels]
        return make_response(response_body, 200)
    
    elif(request.method == 'POST'):
        new_hotel = Hotel(name=request.json.get('name'))
        db.session.add(new_hotel)
        db.session.commit()
        response_body = new_hotel.to_dict(only=('id', 'name'))
        return make_response(response_body, 201)

# GET hotel by id with /hotels/<int:id>
@app.route('/hotels/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def hotel_by_id(id):
    hotel = db.session.get(Hotel, id)

    if hotel:
        if(request.method == 'GET'):
            response_body = hotel.to_dict(rules=('-reviews.hotel', '-reviews.customer'))

            # Add in the association proxy data (The hotel's customers)
            response_body['customers'] = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in hotel.customers]
            
            return make_response(response_body, 200)
        
        if(request.method == 'PATCH'):
            for attr in request.json:
                setattr(hotel, attr, request.json[attr])
            db.session.commit()
            
            response_body = hotel.to_dict(only=('id', 'name'))
            
            return make_response(response_body, 200)
        
        if(request.method == 'DELETE'):
            db.session.delete(hotel)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
    else:
        response_body = {
            "error": "Hotel Not Found"
        }
        return make_response(response_body, 404)

# GET all customers with /customers
@app.route('/customers', methods=['GET', 'POST'])
def all_customers():
    if(request.method == 'GET'):
        customers = Customer.query.all()
        customer_list_with_dictionaries = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in customers]
        return make_response(customer_list_with_dictionaries, 200)
    
    elif(request.method == 'POST'):
        new_customer = Customer(first_name=request.json.get('first_name'), last_name=request.json.get('last_name'))
        db.session.add(new_customer)
        db.session.commit()
        response_body = new_customer.to_dict(only=('id', 'first_name', 'last_name'))
        return make_response(response_body, 201)

# GET customer by id with /customers/<int:id>
@app.route('/customers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def customer_by_id(id):
    customer = db.session.get(Customer, id)

    if customer:
        if(request.method == 'GET'):
            response_body = customer.to_dict(rules=('-reviews.hotel', '-reviews.customer'))

            # Add in the association proxy data (The customer's hotels)
            response_body['hotels'] = [hotel.to_dict(only=('id', 'name')) for hotel in customer.hotels]

            return make_response(response_body, 200)
        
        elif(request.method == 'PATCH'):
            for attr in request.json:
                setattr(customer, attr, request.json[attr])
            db.session.commit()
            response_body = customer.to_dict(only=('id', 'first_name', 'last_name'))
            return make_response(response_body, 200)
        
        if(request.method == 'DELETE'):
            db.session.delete(customer)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
    else:
        response_body = {
            "error": "Customer Not Found"
        }
        return make_response(response_body, 404)

# GET all reviews with /reviews
@app.route('/reviews', methods=['GET', 'POST'])
def all_reviews():
    if(request.method == 'GET'):
        reviews = Review.query.all()
        review_list_with_dictionaries = [review.to_dict(rules=('-hotel.reviews', '-customer.reviews')) for review in reviews]
        return make_response(review_list_with_dictionaries, 200)
    
    elif(request.method == 'POST'):
        new_review = Review(rating=request.json.get('rating'), text=request.json.get('text'), hotel_id=request.json.get('hotel_id'), customer_id=request.json.get('customer_id'))
        db.session.add(new_review)
        db.session.commit()
        response_body = new_review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
        return make_response(response_body, 201)

# GET review by id with /reviews/<int:id>
@app.route('/reviews/<int:id>')
def review_by_id(id):
    review = db.session.get(Review, id)

    if review:
        response_body = review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
        return make_response(response_body, 200)
    else:
        response_body = {
            "error": "Review Not Found"
        }
        return make_response(response_body, 404)

if __name__ == "__main__":
    app.run(port=7777, debug=True)