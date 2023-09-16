import os

import openai
from dotenv import load_dotenv
from flask import Flask, request

from score_request.get_sustainability_score import get_sustainability_score
from story_request.get_story import get_story_api
from utils.check_env_variables import check_env_variables

load_dotenv()
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

@app.route('/get_story')
def get_story():
    product_data = request.get_json()
    return get_story_api(product_data)


@app.route('/get_story_dummy',  methods=['GET'])
def get_story_dummy():
    product_data = {
        "product_id": 0
    }
    return get_story_api(product_data)
