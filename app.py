from flask import Flask
from flask_restful import Api 
from flask_migrate import Migrate
from models.db import db

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/Be_practice"
app.config['SQLALCHEMY_ECHO'] = True


api=Api(app)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)