
import uuid
from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores, items
from schemas import ItemSchema, ItemUpdateSchema, StoreSchema

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:store_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return jsonify(items[item_id])
        except IndexError:
            return jsonify({"message": "store not found"}), 404

    def delete(self, item_id):
        if id in items:
            del items[item_id]
            return jsonify({"message": "store deleted"})
        else:
            abort(404, message="store not found")

    def put(self, item_id):
        item_data = request.get_json()
        if (
            "name" not in item_data
            or "price" not in item_data
        ):
            abort(400, message="missing data")

        # for item in items.values():
        #     if item["store_id"] == item_data["store_id"] and item["name"] == item_data["name"]:
        #         abort(400, message="item already exists")    

        # new_item = {**item_data, "id": item_id}
        # items[item_id] = new_item
        # return jsonify(new_item), 201
        try:
            item = items[item_id]
            item |= item_data
            return item
        except IndexError:
            abort(404, message="item not found")

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) #can return multiple items
    def get(self):
        # return {"items": list(items.values())} # pre @blp.response
        return items.values()
    
    @blp.arguments(ItemSchema)    
    def post(self):
        item_data = request.get_json()
        if("price" not in item_data or "name" not in item_data or "store_id" not in item_data):
            abort(400, message="missing data")

        for item in items.values():
            if item["store_id"] == item_data["store_id"] and item["name"] == item_data["name"]:
                abort(400, message="item already exists")

        item_id = uuid.uuid4().hex
        new_item = {**item_data, "id": item_id}
        items[item_id] = new_item

        return new_item, 201
