import os
from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()#this is going to run only if there is no tables
    #depricated

    with app.app_context():
        db.create_all()


    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(TagBlueprint)

    return app

# @app.get("/store")
# def get_stores():
#     return jsonify({"stores": list(stores.values())})
#     # return {'stores' : stores}


# @app.post("/store")
# def post_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     new_store = {**store_data, "id": store_id}
#     stores[store_id] = new_store
#     return jsonify(new_store), 201


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     item_id = uuid.uuid4().hex

#     if (
#         "store_id" not in item_data
#         or "name" not in item_data
#         or "price" not in item_data
#     ):
#         abort(400, message="missing data")

#     for item in items.values():
#         if item["store_id"] == item_data["store_id"] and item["name"] == item_data["name"]:
#             abort(400, message="item already exists")    

#     new_item = {**item_data, "id": item_id}
#     items[item_id] = new_item
#     return jsonify(new_item), 201


# @app.get("/store/<string:id>")
# def get_store(id):
#     try:
#         return jsonify(stores[id])
#     except IndexError:
#         return jsonify({"message": "store not found"}), 404


# @app.get("/items")
# def get_items():
#     return jsonify({"items": list(items.values())})


# @app.get("/item/<string:id>")
# def get_item_in_store(id):
#     # try:
#     #     return jsonify(items[id])
#     # except IndexError:
#     #     abort(404, message='item not found')
#     if id in items:
#         return jsonify(items[id])
#     else:
#         abort(404, message="item not found")


# @app.delete("/store/<string:id>")
# def delete_store(id):
#     if id in stores:
#         del stores[id]
#         return jsonify({"message": "store deleted"})
#     else:
#         abort(404, message="store not found")


# @app.patch("/store/<string:id>")
# def update_store(id):
#     store_data = request.get_json()
#     if id in stores:
#         store = stores[id]
#         store.update(store_data)
#         return jsonify(store)
#     else:
#         abort(404, message="store not found")