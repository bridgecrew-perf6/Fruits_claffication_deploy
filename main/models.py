from . import db

class Fruit(db.Model):
    __tablename__ = 'fruit'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    peel_color = db.Column(db.Integer)
    flesh_color = db.Column(db.Integer)
    texture = db.Column(db.Integer)
    size = db.Column(db.Integer)
    name = db.Column(db.String(128))
    