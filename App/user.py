from product import Product

class User:

    @staticmethod
    def signup(request, db, jsonify, pbkdf2_sha256, session):
        # get user posted info
        posted_data = request.get_json()
        # checking if posted info is null or not        
        if not posted_data["name"] or not posted_data["email"] or not posted_data["age"] or not posted_data["gender"] or not posted_data["password"]:
            return jsonify({"error": "incomplete signup info"}), 400
        # connect to userinfo collection
        collection = db.user_info
        # check if user email already exist
        if collection.find_one({"email": posted_data["email"]}):
            return jsonify({"error": "email already exist"}), 400
        # create user model object
        user = {
            "name": posted_data["name"],
            "email": posted_data["email"],
            "age" : posted_data["age"],
            "gender" : posted_data["gender"],
            "password": pbkdf2_sha256.encrypt(posted_data["password"]),
            "cart_items" : []
        }
        # insert user data into database
        res = collection.insert_one(user)
        if res:
        # create user session
            session["user"] = {
                "_id" : res.inserted_id,
                "name": user["name"],
                "email": user["email"],
                "age" : posted_data["age"],
                "gender" : posted_data["gender"]
                }
            session["logged_in"] = True
            return jsonify({"message" : "Signed up successfully"}) , 200
        else:
        # if insertion of data fails
            return jsonify({"error": "signup failed"}) , 400


    @staticmethod
    def login(request, db, jsonify, pbkdf2_sha256, session):
        posted_data = request.get_json()
        if not posted_data["email"] or not posted_data["password"]:
            return jsonify({"error": "incomplete login info"}), 400
        collection = db.user_info
        data = collection.find_one({"email" : posted_data["email"]})
        if data and pbkdf2_sha256.verify(posted_data["password"],data["password"] ):
            session["user"] = {
                "_id" : data["_id"],
                "name": data["name"],
                "email": data["email"],
                "age" : data["age"],
                "gender" : data["gender"]
                }
            session["logged_in"] = True
            print(session)
            return jsonify({"message" : "logged in successfully"}) , 200
        return jsonify({"message" : "invalid login credential"}) , 400
    

    @staticmethod
    def addToCart(db, user_id, category, product_id):
        product , statusCode = Product.fetchProduct(db,category , product_id)
        product["_id"] = str(product["_id"]) 
        userCollection = db["user_info"]
        user = userCollection.find_one({"_id" : user_id})
        cart = user["cart_items"]
        cart.append({"category" : category , "product" : product})
        userCollection.update_one({"_id" : user_id} , {"$set":{"cart_items" : cart}})
        return {"message" : "item added successfully"} , 200
    


    