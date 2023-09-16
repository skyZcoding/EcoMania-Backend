from story_request.context_mappings import context_mappings
from story_request.openai_utils import get_story_from_openai


def get_basic_context(product_id):
    context = context_mappings[product_id]["context"]
    return context



def get_story_api(product_data):
    product_id = product_data["product_id"]
    color = "blue"
    basic_context = get_basic_context(product_id)
    prompt = basic_context.format(color=color)
    return get_story_from_openai(prompt)
