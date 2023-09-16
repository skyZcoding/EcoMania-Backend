import os


def check_env_variables():
    openai_key = os.environ.get('OPENAI_KEY', None)
    if openai_key is None:
        raise RuntimeError("No OPENAI_KEY in environmental variables")
    print("Found OPENAI_KEY!")
