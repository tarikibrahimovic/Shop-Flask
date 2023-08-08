from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("StoreModel", back_populates="items")

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {"name": self.name, "price": self.price}
    
    @classmethod
    def find_by_name(cls, name):
        # return ItemModel.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1
    
    @classmethod
    def find_all(cls):
        # return ItemModel.query.all() # SELECT * FROM items
        return cls.query.all() # SELECT * FROM items
    
    def save_to_db(self):
        # session.add(self)
        # session.commit()
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        # session.delete(self)
        # session.commit()
        db.session.delete(self)
        db.session.commit()