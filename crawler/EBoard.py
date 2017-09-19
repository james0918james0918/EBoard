from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import execute
from execute import try_login
from execute import get_ceiba

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('acc', type=str)
parser.add_argument('pwd', type=str)

class Eboard(Resource):
	def post(self):
		args = parser.parse_args()
		the_json = get_ceiba(args['acc'], args['pwd'])
		return the_json


class Test(Resource):
	def get(self, a, p):
		the_json = get_ceiba(a, p)
		return the_json


class Login(Resource):
	def post(self):
		args = parser.parse_args()
		login_result = try_login(args['acc'], args['pwd'])

		if login_result:
			return "successful", 200
		else:
			return "unauthorized login", 200


class Crawlers(Resource):
	def get(self):
		execute.main()
		return 200


class Crawler(Resource):
	def get(self, cid):
		if cid < 1 or cid > 13:
			return "Invalid Crawler ID", 401
		elif cid <= 8:
			announ = AnnounCrawler()

			{
				'1': get_activities,
				'2': get_calendar,
				'3': get_extra_curr_announ,
				'4': get_management_department,
				'5': get_general_affairs,
				'6': get_academic_affairs,
				'7': get_student_affairs,
				'8': get_extra_curr_today
			}[cid](announ)

			return "successful", 200
		elif cid >= 9 and cid <= 11:
			course = CourseCrawler()

			{
				'9': get_yktasySDM,
				'10': get_yktasyIS,
				'11': get_yktasyDS
			}[cid](course)

			return "successful", 200
		else:
			facility = FacilityCrawler()

			{
				'12': get_lib,
				'13': get_gym
			}[cid](facility)

			return "successful", 200


##
## Actually setup the Api resource routing here
##
api.add_resource(Eboard, '/ceiba')
api.add_resource(Test, '/test/<a>/<p>')
api.add_resource(Login, '/login')
api.add_resource(Crawlers, '/crawlers')
api.add_resource(Crawler, '/crawler/<cid>')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
