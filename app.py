from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__) 
api = Api(app)

@api.route('/connect')
class Connect(Resource) :
    def get(self) :
        return {"connect" : "success"}

@api.route('/usermaps') 
class UserMaps(Resource):
    def get(self):
        return {"connect" : "success"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)