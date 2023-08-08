import uuid
from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return jsonify(stores[store_id])
        except IndexError:
            return jsonify({"message": "store not found"}), 404

    def delete(self, store_id):
        if store_id in stores:
            del stores[store_id]
            return jsonify({"message": "store deleted"})
        else:
            abort(404, message="store not found")

@blp.route("/store")
class StoreList(MethodView):
    @blp.arguments(StoreSchema)
    def post(self):
        store_data = request.get_json()
        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": store_id}
        stores[store_id] = new_store
        return jsonify(new_store), 201
    
    def get(self):
        return jsonify({"stores": list(stores.values())})