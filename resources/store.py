import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from resources.schemas import ItemSchema, StoreSchema
from models.store import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return "", 204


@blp.route("/store")
class StoreList(MethodView):
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError as e: #IntegrityError is when you try to insert a duplicate item
            abort(400, message="item already exists")
        except SQLAlchemyError as e:
            abort(400, message="item already exists")
        return store

    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
