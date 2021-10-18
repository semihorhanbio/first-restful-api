from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, function_name):
    if function_name in ["add", "subtract", "multiply"]:
        if "x" not in posted_data or "y" not in posted_data:
            return 301 # missing parameter
        return 200
    elif function_name == "division":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"] == 0):
            return 302
        else:
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
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
        
        #Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, "subtract")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)
        
        # If i am here, then status code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
            
        # Step 2: Subtract the posted data
        ret_map = {
            'Message': x - y,
            "Status Code": 200
        }
        return jsonify(ret_map)


class Multiply(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
        
        #Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, "multiply")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)
        
        # If i am here, then status code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
            
        # Step 2: multiply the posted data
        ret_map = {
            'Message': x * y,
            "Status Code": 200
        }
        return jsonify(ret_map)
    

class Divide(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()
        
        #Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, "division")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)
        
        # If i am here, then status code == 200
        x = int(postedData["x"])
        y = int(postedData["y"])
            
        # Step 2: multiply the posted data
        ret_map = {
            'Message': x / y,
            "Status Code": 200
        }
        return jsonify(ret_map)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)