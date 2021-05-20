from models.db import db
from datetime import datetime


class Food(db.Model):
    __tablename__='foods'
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(80))
    catergory = db.Column(db.sting(225))
    calories = db.Column(db.Interger)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    

    def __init__(self, name, category, calories):
        self.name= name 
        self.catergory = category
        self.calories = calories



    def json(self):
        return{"id":self.id,
                "name": self.name,
                "category": self.catergory,
                "calories": self.calories, 
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Food.query.all()


    @classmethod
    def find_by_id(cls, id):
        return Food.query.filter_by(id=id).first()