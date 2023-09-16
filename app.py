from flask import Flask, request

from score_request.get_sustainability_score import get_sustainability_score

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Feel the power of devops!'


@app.route('/get_sustainability_score')
def get_sust_score():
    product_data = request.get_json()
    return get_sustainability_score(product_data["product_ids"])
