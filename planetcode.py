from flask import Flask 
from flask_restful import Api, Resource 

app = Flask(__name__)
api = Api(app)

class test(Resource):
	def get(self):
		return {"data":"Hello"}
api.add_resource(test,"/hello")

if __name__ == "__main__":
	app.run(debug=True)