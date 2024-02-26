from flask import Flask,jsonify,request
from flask_cors import CORS
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Peerapat_Sent_work:u1LqjH7nGhbIlnTC@cluster0.aj79tau.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
app = Flask(__name__)
CORS(app)

client.admin.command('ping')
db = client["products"]
collection = db["data_product"]

@app.route("/")
def greet():
      return "<p>Hello!!!</p>"

@app.route("/products",methods=["GET"])
def get_all_products():
      d = list(collection.find())
      return jsonify(d),200

@app.route("/products",methods=["POST"])
def post_products():
    data = request.get_json();
    id = collection.find_one({"_id":data.get("_id")})
    if id:
        return jsonify({"error":"Cannot create new products"}),500
    collection.insert_one(data)
    return jsonify(data),200

@app.route("/products/<int:data_products>",methods=["PUT"])
def put_products(data_products):
    data = request.get_json();
    id = collection.find_one({"_id":data_products})
    if not id:
        return jsonify({"error":"products not found"}),404
    collection.update_one({"_id": data_products}, {"$set": data})
    return jsonify(data),200

@app.route("/products/<int:data_products>",methods=["DELETE"])
def delete_products(data_products):
    id = collection.find_one({"_id":data_products})
    if not id:
        return jsonify({"error":"products not found"}),404
    collection.delete_one({"_id": data_products})
    return jsonify({"message":"products deleted successfully"}),200


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)