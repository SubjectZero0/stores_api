from flask import Flask
from resources.db import db

class StoreModel(db.Model):

    __tablename__='store'

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, unique=True, nullable=False)
    # store_tags = db.Column()
    items = db.relationship('ItemModel', back_populates='store', lazy='dynamic')