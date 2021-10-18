from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, function_name):
    if function_name == "add":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        return 200

class Add(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
        
        #Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, "add")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)
        
        # If i am here, then status code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
            
        # Step 2: Add the posted data
        ret_map = {
            'Message': x + y,
            "Status Code": 200
        }
        return jsonify(ret_map)

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)