class Product:
    @staticmethod
    def fetchCategory(request, db, jsonify):
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
        
    @staticmethod
    def fetchProduct(request, db, jsonify):
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
        
    @staticmethod
    def fetchTenProductEachCategory(request, db, jsonify):
        collections = db.list_collection_names()
        mainDict = {}
        for collection in collections:
            if(collection[0:9] == "category_"):
                data = list(db[collection].find({}).limit(10))
                for document in data:
                    document["_id"] = str(document["_id"])
                mainDict[collection[9:]] = data
        return jsonify(mainDict), 200
                