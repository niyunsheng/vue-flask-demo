from flask import Flask
from flask import request
from flask import jsonify

from flask_restful import Api, Resource

app = Flask(__name__)

# api = Api(app)
# class Add(Resource):

#     def get(self):
        
#         return {'code':200,'msg':'ok'}

# api.add_resource(Add, '/add2/')

@app.route('/add')
def add():
    v1 = request.args.get("v1")
    v2 = request.args.get("v2")
    print(request.args)
    print({'code':200,'msg':'ok','data':str(int(v1)+int(v2))})
    return jsonify({'code':200,'msg':'ok','data':str(int(v1)+int(v2))})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')