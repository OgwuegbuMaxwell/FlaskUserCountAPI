from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import os
from pymongo import MongoClient



app = Flask(__name__)
api = Api(app)

# Accessing database
client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

# Initialize the user count if not already set
if UserNum.count_documents({}) == 0:
    UserNum.insert_one({'num_of_users': 0})
    
    
class Visit(Resource):
    def get(self):
        try:
            user_record = UserNum.find_one({})
            prev_num = user_record['num_of_users']
            new_num = prev_num + 1
            UserNum.update_one({}, {"$set": {"num_of_users": new_num}})
            return str("Hello user " + str(new_num))
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Visit, "/hello")

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
