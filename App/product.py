class Product:
    @staticmethod
    def fetchCategory(db, category):
        collection = db[f"category_{category}"]
        data = list(collection.find({}))
        if data:
            for document in data:
                document["_id"] = str(document["_id"])
            return data , 200
        else:
            return {"message" : "category does not exist"} , 404 
        
    @staticmethod
    def fetchProduct(db, category, product_id):
        collection = db[f"category_{category}"]  
        data = collection.find_one({"id" : int(product_id)})
        if data:
            data["_id"] = str(data["_id"])
            return data , 200
        else:
            return {"message" : "item does not exist"} , 404
        
    @staticmethod
    def fetchTenProductEachCategory(db):
        collections = db.list_collection_names()
        mainDict = {}
        for collection in collections:
            if(collection[0:9] == "category_"):
                data = list(db[collection].find({}).limit(10))
                for document in data:
                    document["_id"] = str(document["_id"])
                mainDict[collection[9:]] = data
        return mainDict, 200
              