import time, requests
from flask import Blueprint, redirect, current_app, request, render_template
from bs4 import BeautifulSoup


bp = Blueprint('routes', __name__)


def init_app(app):
    app.register_blueprint(bp)


@bp.route('/')
def index():
    time.sleep(5)
    sequenceserver = current_app.config['INDEX']
    return redirect(sequenceserver, 302)


@bp.route('/id/<id>', methods=['POST', 'GET'])
def receive_id(id):
    if request.method == 'POST':
        blast_result = f"{current_app.config['INDEX']}/{id}"
        response = requests.get(blast_result)
        with open('templates/blast_doc.html', 'w') as file:
            file.write(response.text)
    
        return id
    
    if request.method == 'GET':
        return render_template('blast_doc.html')