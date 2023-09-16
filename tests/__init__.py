import os

import openai
from dotenv import load_dotenv

from utils.check_env_variables import check_env_variables


check_env_variables()
openai.api_key = os.getenv("OPENAI_KEY")