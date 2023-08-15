from marshmallow import Schema, fields, validate

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)

class ItemUpdateSchema(Schema):
    name = fields.String()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)# load_only=True means that this field is only for loading, not for dumping
    store = fields.Nested(PlainStoreSchema(), dump_only=True)# dump_only=True means that this field is only for dumping, not for loading
    tags = fields.Nested(PlainTagSchema(), many=True, dump_only=True)# many=True means that this field is a list of objects
    #dumping is converting an object to a dictionary

class StoreSchema(PlainStoreSchema):
    items = fields.Nested(PlainItemSchema(), many=True, dump_only=True)
    tags = fields.Nested(PlainTagSchema(), many=True, dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.Nested(PlainItemSchema(), many=True, dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.String()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)