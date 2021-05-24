from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello') # 라우트 함수
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'

