from image_request.img_prompt_mappings import get_basic_prompt_for_monster_img
from image_request.openai_img_utils import get_image_url_from_openai


def get_image_url_api(monster_data):
    monster_id = monster_data["monster_id"]
    color = monster_data.get("color", "blue")
    basic_img_prompt = get_basic_prompt_for_monster_img(monster_id)
    prompt = basic_img_prompt.format(color=color)
    return get_image_url_from_openai(prompt)
