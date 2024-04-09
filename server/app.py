#!/usr/bin/env python3
import ipdb

from flask import Flask, make_response, request
from flask_migrate import Migrate

from flask_restful import Api, Resource

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

api = Api(app)

class AllHotels(Resource):

    def get(self):
        hotels = Hotel.query.all()
        response_body = [hotel.to_dict(only=('id', 'name')) for hotel in hotels]
        return make_response(response_body, 200)
    
    def post(self):
        new_hotel = Hotel(name=request.json.get('name'))
        db.session.add(new_hotel)
        db.session.commit()
        response_body = new_hotel.to_dict(only=('id', 'name'))
        return make_response(response_body, 201)
    
api.add_resource(AllHotels, '/hotels')

class HotelByID(Resource):

    def get(self, id):
        hotel = db.session.get(Hotel, id)

        if hotel:
            response_body = hotel.to_dict(rules=('-reviews.hotel', '-reviews.customer'))

            # Add in the association proxy data (The hotel's customers)
            response_body['customers'] = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in hotel.customers]
            
            return make_response(response_body, 200)
        
        else:
            response_body = {
                'error': "Hotel Not Found"
            }
            return make_response(response_body, 404)
        
    def patch(self, id):
        hotel = db.session.get(Hotel, id)

        if hotel:
            for attr in request.json:
                setattr(hotel, attr, request.json[attr])
            db.session.commit()
            
            response_body = hotel.to_dict(only=('id', 'name'))
            
            return make_response(response_body, 200)

        else:
            response_body = {
                'error': "Hotel Not Found"
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        hotel = db.session.get(Hotel, id)

        if hotel:
            db.session.delete(hotel)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                'error': "Hotel Not Found"
            }
            return make_response(response_body, 404)
    
api.add_resource(HotelByID, '/hotels/<int:id>')

class AllCustomers(Resource):

    def get(self):
        customers = Customer.query.all()
        customer_list_with_dictionaries = [customer.to_dict(only=('id', 'first_name', 'last_name')) for customer in customers]
        return make_response(customer_list_with_dictionaries, 200)
    
    def post(self):
        new_customer = Customer(first_name=request.json.get('first_name'), last_name=request.json.get('last_name'))
        db.session.add(new_customer)
        db.session.commit()
        response_body = new_customer.to_dict(only=('id', 'first_name', 'last_name'))
        return make_response(response_body, 201)
    
api.add_resource(AllCustomers, '/customers')

class CustomerByID(Resource):

    def get(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            response_body = customer.to_dict(rules=('-reviews.hotel', '-reviews.customer'))

            # Add in the association proxy data (The customer's hotels)
            response_body['hotels'] = [hotel.to_dict(only=('id', 'name')) for hotel in customer.hotels]

            return make_response(response_body, 200)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)
        
    def patch(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            for attr in request.json:
                setattr(customer, attr, request.json[attr])
            
            db.session.commit()
            response_body = customer.to_dict(only=('id', 'first_name', 'last_name'))
            return make_response(response_body, 200)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)
         
    def delete(self, id):
        customer = db.session.get(Customer, id)

        if customer:
            db.session.delete(customer)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                'error': "Customer Not Found"
            }
            return make_response(response_body, 404)

api.add_resource(CustomerByID, '/customers/<int:id>')

class AllReviews(Resource):
    
    def get(self):
        reviews = Review.query.all()
        review_list_with_dictionaries = [review.to_dict(rules=('-hotel.reviews', '-customer.reviews')) for review in reviews]
        return make_response(review_list_with_dictionaries, 200)
    
    def post(self):
        new_review = Review(rating=request.json.get('rating'), text=request.json.get('text'), hotel_id=request.json.get('hotel_id'), customer_id=request.json.get('customer_id'))
        db.session.add(new_review)
        db.session.commit()
        response_body = new_review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
        return make_response(response_body, 201)
    
api.add_resource(AllReviews, '/reviews')

class ReviewByID(Resource):

    def get(self, id):
        review = db.session.get(Review, id)

        if review:
            response_body = review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
            return make_response(response_body, 200)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)
        
    def patch(self, id):
        review = db.session.get(Review, id)

        if review:
            for attr in request.json:
                setattr(review, attr, request.json.get(attr))
            
            db.session.commit()
            response_body = review.to_dict(rules=('-hotel.reviews', '-customer.reviews'))
            return make_response(response_body, 200)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        review = db.session.get(Review, id)

        if review:
            db.session.delete(review)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                "error": "Review Not Found"
            }
            return make_response(response_body, 404)

api.add_resource(ReviewByID, '/reviews/<int:id>')

if __name__ == "__main__":
    app.run(port=7777, debug=True)