from flask import request, Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET', 'POST'])
def api_hello():
    if request.method == 'GET':
        return {'message': 'Hello World'}
    elif request.method == 'POST':
        return {'message': 'Hello World POST'}