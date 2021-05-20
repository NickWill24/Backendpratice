from flask_restful import Resource
from flask import request
from models.food import Food
from models.db import db


class Foods(Resource):
    def get(self):
        data = Food.find_all()
        results = [u.json() for u in data]
        return results


    def post(self):
        data= request.get_json()
        food= Food(**data)
        food.create()
        return food.json(),201


class SingleFood(Resource):
    def get(self,id):
        food = Food.find_by_id(id)
        return food.json()


    def delete(self, id):
        food = Food.find_by_id(id)
        db.session.delete(food)
        db.session.commit()
        return{"msg": 'Food deleted', 'payload': food.id}


    def put(self,id):
        food = Food.find_by_id(id)
        data = request.get_json()
        for key in data:
            setattr(food,key,data[key])
        db.session.commit()
        return food.json()