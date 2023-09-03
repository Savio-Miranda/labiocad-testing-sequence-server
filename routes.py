import time
from flask import Blueprint, redirect, current_app


bp = Blueprint('routes', __name__)


def init_app(app):
    app.register_blueprint(bp)


@bp.route('/')
def index():
    time.sleep(5)
    sequenceserver = current_app.config['INDEX']
    return redirect(sequenceserver, 302)


@bp.route('/id/<id>', methods=['POST'])
def receive_id(id):
    print(f"recebeu isso aqui {id}")
    return id