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

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)