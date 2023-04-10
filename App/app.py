from flask import Flask, render_template, jsonify, request, session, redirect
from user import User
import os
from dotenv import load_dotenv
from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient
from flask_session import Session
load_dotenv()

app = Flask(__name__)
app.secret_key = b'\x16<\xe2\x13C\xaf\x89\xb0\xb7|\xf2\xcf\xfb<\x02\xad'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Mongodb connection
# client = MongoClient('localhost', 27017)
client = MongoClient(os.getenv('CONNECTION_STRING'))
db = client.E_Commerce

# routes
@app.get("/login/")
def handle_login_page():
    return render_template("login.html")

@app.get("/signup/")
def handle_signup_page():
    return render_template("signup.html")

@app.get("/")
def handle_home_page():    
    if session:
        # fetch according to gender
        # fetch 10 products of every category
        return render_template("home.html")
    else:
        return redirect("/login")

@app.get("/category")
def handle_category_page():    
    if session:
        # fetch according to gender
        # fetch 10 products of every category
        return render_template("home.html")
    else:
        return redirect("/login")




# api 
@app.post("/api/user/signup")
def handle_signup():
    return User.signup(request, db, jsonify, pbkdf2_sha256, session)

@app.post("/api/user/login")
def handle_login():
    return User.login(request, db, jsonify, pbkdf2_sha256, session)

@app.route("/api/user/signout")
def handle_signout():
    session.clear()
    return redirect("/login")

@app.get("/api/product")
def handle_product():
    args = request.args
    category = args.get("category")    
    product_id = int(args.get("product_id"))
    collection = db[f"category_{category}"]   
    data = collection.find_one({"id" : product_id})
    if data:
        data["_id"] = str(data["_id"])
        return jsonify(data) , 200
    else:
        return jsonify({"message" : "item does not exist"}) , 404


@app.route("/api/fetch_category")
def handle_fetch_category():
    args = request.args
    category = args.get("category")    
    collection = db[f"category_{category}"]
    data = list(collection.find({}))
    if data:
        for document in data:
            document["_id"] = str(document["_id"])
        return jsonify(data) , 200
    else:
        return jsonify({"message" : "category does not exist"}) , 404

# create api to fetch 10 product from every category

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

