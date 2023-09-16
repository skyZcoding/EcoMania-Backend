import os

from dotenv import load_dotenv


def check_env_variables():
    load_dotenv()
    openai_key = os.environ.get('OPENAI_KEY', None)
    if openai_key is None:
        raise RuntimeError("No OPENAI_KEY in environmental variables")
    print("Found OPENAI_KEY!")
