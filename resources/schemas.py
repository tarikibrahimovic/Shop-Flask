from marshmallow import Schema, fields, validate

class PlainItemSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    


class ItemUpdateSchema(Schema):
    name = fields.String()
    price = fields.Float()


class PlainStoreSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema, dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.Nested(PlainItemSchema, many=True, dump_only=True)