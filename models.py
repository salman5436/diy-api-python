from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask App
app = Flask(__name__)

# Set some App configs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python_api'

# Init a db
db = SQLAlchemy(app)

class Widget(db.Model):
    __tablename = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    wodgets = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'wodgets': self.wodgets,
            'quantity': self.quantity
        }
    

    def __repr__(self):
        return f'Widget(id={self.id}, name="{self.name}", wodgets={self.wodgets}, quantity={self.quantity}'
