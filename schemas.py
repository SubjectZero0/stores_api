from marshmallow import Schema, fields

class BaseItemSchema(Schema):
    #base class to avoid infinite Nesting
    item_id = fields.Str(dump_only=True)
    item_title = fields.Str(required=True)
    item_price = fields.Float(required=True)
    item_desc = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    item_title = fields.Str()
    item_price = fields.Float()
    item_desc = fields.Str()

class BaseStoreSchema(Schema):
    #base class to avoid infinite Nesting
    store_id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)

class ItemSchema(Schema):
    _store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(BaseStoreSchema(), dump_only=True)

class StoreSchema(Schema):
    items = fields.Nested(BaseItemSchema(), dump_only=True)