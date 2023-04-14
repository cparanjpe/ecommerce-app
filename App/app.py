from flask import Flask, render_template, jsonify, request, session, redirect
from user import User
from product import Product
import os
from dotenv import load_dotenv
from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient
from flask_session import Session
from bson.objectid import ObjectId
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
        return render_template("home.html")
    else:
        return redirect("/login")

@app.get("/details/<category>/<product_id>")
def handle_details_page(category , product_id):    
    if session:
        (data,statusCode) = Product.fetchProduct(db, category, product_id)
        return render_template("details.html" , productInfo = data , statusCode = statusCode)
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

# /api/fetch_product/<category>/<product_id>
@app.get("/api/fetch_product/<category>/<product_id>")
def handleFetchProduct(category , product_id):
    (data,statusCode) = Product.fetchProduct(db, category, product_id)
    return jsonify(data) , statusCode

# /api/fetch_category/<category>
@app.get("/api/fetch_category/<category>")
def handleFetchCategory(category):
    (data,statusCode) = Product.fetchCategory(db, category)
    return jsonify(data) , statusCode

# /api/homepage_content
@app.get("/api/homepage_content")
def handle_home_page_content():
    (data,statusCode) = Product.fetchTenProductEachCategory(db)
    return jsonify(data) , statusCode

# /api/add_to_cart/<user_id>/<category>/<product_id>
@app.post("/api/add_to_cart/<user_id>/<category>/<product_id>")
def handle_add_to_cart(user_id,category,product_id):
    (data,statusCode) = User.addToCart(db, ObjectId(user_id), category, product_id)
    return jsonify(data) , statusCode

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)