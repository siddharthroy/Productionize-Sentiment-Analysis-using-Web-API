from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import TrainedModel as TM

web_app = Flask(__name__)
web_api = Api(web_app)

class myClass(Resource):
    def post(self):
        ip_dict = request.get_json()
        ip_comment = ip_dict['comment']
        op_dict = {'is_comment_good':str(TM.is_comment_good(ip_comment))}  # 'ndarray' is not JSON serializable. Can use np.asscalar()
        return jsonify(op_dict)


web_api.add_resource(myClass, "/is_good")


