from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    #lazy="dynamic" means that self.items is a query builder, not a list of items, and it's not going to fetch unless we want it to
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")