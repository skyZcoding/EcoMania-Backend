import os


def check_env_variables():
    openai_key = os.environ.get('TEST_ENV_VARIABLE', None)
    if openai_key is None:
        raise RuntimeError("No TEST_ENV_VARIABLE in environmental variables")
    print("Found TEST_ENV_VARIABLE!")
