import os

import openai
from flask import Flask, request

from image_request.get_image import get_image_url_api
from score_request.get_popular_products import get_popular_products
from score_request.get_sustainability_score import get_sustainability_score
from story_request.get_story import get_story_api
from utils.check_env_variables import check_env_variables

check_env_variables()

openai.api_key = os.getenv("OPENAI_KEY")
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Feel the power of devops!'


@app.route('/get_sustainability_score')
def get_sust_score():
    product_data = request.get_json()
    return get_sustainability_score(product_data["product_ids"])


@app.route('/get_story', methods=['POST'])
def get_story():
    monster_data = request.get_json()
    return get_story_api(monster_data)


@app.route('/get_monster_image_url')
def get_monster_image_url():
    monster_data = request.get_json()
    return get_image_url_api(monster_data)


@app.route('/get_story_dummy', methods=['GET'])
def get_story_dummy():
    monster_data = {
        "monster_id": 999
    }
    return get_story_api(monster_data)


@app.route('/get_image_url_dummy', methods=['GET'])
def get_image_dummy():
    monster_data = {
        "monster_id": 999
    }
    return get_image_url_api(monster_data)


@app.route('/get_popular_products')
def get_popular_prods():
    return get_popular_products(n_products=50)
