from flask import Flask, render_template, jsonify, request, session, redirect
from user import User
from product import Product
import os
# from dotenv import load_dotenv
from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient
from flask_session import Session
from bson.objectid import ObjectId
import json
# load_dotenv()
import certifi
from datetime import datetime
from flask_mail import Mail,Message

app = Flask(__name__)
app.secret_key = b'\x16<\xe2\x13C\xaf\x89\xb0\xb7|\xf2\xcf\xfb<\x02\xad'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Mongodb connection
# client = MongoClient('localhost', 27017)
ca = certifi.where()
client = MongoClient('mongodb+srv://user:userpass@cluster0.ocdnjgz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.E_Commerce

#email config
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='eazymart23@outlook.com'
app.config['MAIL_PASSWORD']='thck@2023'
mail = Mail(app)

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
        return render_template("details.html" ,category=category,product_id=product_id, productInfo = data , statusCode = statusCode)
    else:
        return redirect("/login") 

@app.get("/cart")
def handle_cart_page():    
    if session:
        return render_template("cart.html")
    else:
        return redirect("/login") 

@app.get("/checkout")
def handle_checkout_page():
    if session:
        return render_template("checkout.html")
    else:
        return redirect("/login")

@app.get("/addorder/<order_total>")
def handle_addorder_page(order_total):
    if session:
        # orderCollection = db.create_collection('customer_orders')

        
        orderCollection = db['customer_orders']
       
        collection = db[f"user_info"]  
        data = collection.find_one({"_id" : session.get('user')["_id"]})
        order = {
            'user_id':session.get('user')["_id"],
            'order_total':order_total,
            'cart_items':data["cart_items"],
            'date':datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        result = orderCollection.insert_one(order)
        email = session.get('user')["email"]
        # print(email)
        recipients = []
        recipients.append(email)
        msg = Message('Order confirmation : EazyMart',sender='eazymart23@outlook.com',recipients=recipients)
        msg.body = "Payment for order received ! Order should be delivered in 7-8 business days ! Thanks for shopping with us."
        mail.send(msg)
        return redirect("/myorders")

    else:
        return redirect("/login")

# @app.get("/deletecollection")
# def handle_delete_collection():
#     mycollection = db['customer_orders']
#     result = mycollection.delete_many({})
#     print(result)
@app.get("/myorders")
def handle_myorders_page():
    orderCollection = db['customer_orders']
    user_id = session.get('user')["_id"]
    orders = orderCollection.find({'user_id':user_id})  
    order_items = []
    for order in orders:
        order_items.append(order)  
    return render_template("myorders.html", orders = order_items)

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
    return redirect("/login") , 200

@app.get("/api/fetch_product/<category>/<product_id>")
def handleFetchProduct(category , product_id):
    (data,statusCode) = Product.fetchProduct(db, category, product_id)
    return jsonify(data) , statusCode

@app.get("/api/fetch_category/<category>")
def handleFetchCategory(category):
    (data,statusCode) = Product.fetchCategory(db, category)
    return jsonify(data) , statusCode

@app.get("/api/homepage_content")
def handle_home_page_content():
    (data,statusCode) = Product.fetchTenProductEachCategory(db)
    return jsonify(data) , statusCode

@app.get("/api/add_to_cart/<category>/<product_id>")
def handle_add_to_cart(category,product_id):
    (data,statusCode) = User.addToCart(db, ObjectId(session.get('user')["_id"]), category, product_id)
    return jsonify(data) , statusCode

@app.get("/api/fetch_cart_items")
def handle_fetch_cart_items():    
    (data , statusCode) = Product.fetchCartItems(db, session)
    return jsonify(data) , 200
    
@app.get("/api/remove_item_from_cart/<product_id>")
def handle_remove_item_from_cart(product_id):
    (data , statusCode) = Product.removeItem(db, session, product_id)
    return jsonify(data) , 200

@app.get("/api/fetch_category_menu")
def handle_category_menu():
    return jsonify(db.list_collection_names()) , 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)