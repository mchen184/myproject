from flask import Flask 
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UserUpdate(db.Model):
	first_name = db.Column(db.String(100),nullable=False)
	last_name = db.Column(db.String(100),nullable=False)
	userid = db.Column(db.String(100), primary_key=True,nullable=False)
	groups = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return f"Record(first_name = {first_name}, last_name = {last_name}, userid = {userid}, groups = {groups})"
db.create_all()

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("first_name",type=str,required=True)
user_put_args.add_argument("last_name",type=str,required=True)
user_put_args.add_argument("userid",type=str,required=True)
user_put_args.add_argument("groups",type=str,required=True)

# post 
user_post_args = reqparse.RequestParser()
user_post_args.add_argument("first_name",type=str,required=True)
user_post_args.add_argument("last_name",type=str,required=True)
user_post_args.add_argument("userid",type=str,required=True)
user_post_args.add_argument("groups",type=str,required=True)

##

resource_fields = {
	'first_name': fields.String,
	'last_name': fields.String,
	'userid':fields.String,
	'groups':fields.String
}

class Record(Resource):
	@marshal_with(resource_fields)
	def get(self,uid):
		result = UserUpdate.query.filter_by(userid=uid).first()
		if not result:
			abort(404,message = "No user found")
		return result 

	@marshal_with(resource_fields)
	# new user added 
	def post(self,uid):
		args = user_post_args.parse_args()
		result = UserUpdate.query.filter_by(userid=uid).first()
		if result:
			abort(409, message="User already exists")
		user = UserUpdate(first_name=args['first_name'],last_name=args['last_name'],userid=uid,groups=args['groups'])
		db.session.add(user)
		db.session.commit()
		return user,201

	def delete(self,uid):
		abort_if_user_id_doesnt_exists(uid)
		del users[uid]
		return '',204

# update user 
	@marshal_with(resource_fields)
	def put(self,uid):
		args = user_put_args.parse_args()
		result = UserUpdate.query.filter_by(userid=uid).first()
		if not result:
			abort (404, message =" No valid user found")
		if args['first_name']:
			result.first_name = args['first_name']
		if args['last_name']:
			result.last_name = args['last_name']
		if args['groups']:
			result.groups = args['groups']

		db.session.commit()
		return result

	

class getGroups(Resource):
	def getgroup(self,gid):
		args = user_post_args.parse_args()
		result = UserUpdate.query.filter_by(groups=gid).first()
		for user in users:
			if not result:
				abort (404, message="No group found")
		return 
		
	def __repr__(self):
		return f"Record(first_name = {first_name}, last_name = {last_name}, userid = {userid}, groups = {groups})"

api.add_resource(Record, "/users/<string:uid>")
api.add_resource(getGroups, "/groups<string:group>")
#api.add_resource(Record,"/groups/<string:gid>")
if __name__ == "__main__":
	app.run(debug=True)