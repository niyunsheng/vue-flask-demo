from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS # 允许跨源请求
# 如果不允许跨源请求的话，nodejs服务在同一台服务器的话，就会报错
# https://stackoverflow.com/questions/20035101/why-does-my-javascript-code-receive-a-no-access-control-allow-origin-header-i



app = Flask(__name__)
CORS(app)

# restful-api，暂时不知道如何传参数
# from flask_restful import Api, Resource
# api = Api(app)
# class Add(Resource):
#     def get(self):
#         return {'code':200,'msg':'ok'}
# api.add_resource(Add, '/add2/')

@app.route('/add')
def add():
    v1 = request.args.get("v1")
    v2 = request.args.get("v2")
    operate = request.args.get("operate")
    print(request.args)
    if not v1:
        v1 = '0'
    if not v2:
        v2 = '0'
    return str(eval(v1+operate+v2))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')