from flask import Flask
from resources.db import db

class ItemModel(db.Model):
    #Database model for Items.
    __tablename__='items'

    item_id = db.Column(db.Integer, primary_key=True)
    item_title = db.Column(db.String(100), unique=True, nullable=False)
    item_desc = db.Column(db.String(500))
    item_price = db.Column(db.Float(precision=2), nullable=False)

    # item_tags = db.Column()

    _store_id = db.Column(db.Integer, db.ForeignKey('StoreModel.store_id'), unique = False, nullable = False)
    store = db.relationship('StoreModel', back_populates='items')