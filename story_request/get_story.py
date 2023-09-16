from story_request.context_mappings import get_basic_context_for_monster
from story_request.openai_utils import get_story_from_openai


def get_story_api(monster_data):
    monster_id = monster_data["monster_id"]
    color = monster_data.get("color", "blue")
    your_name = monster_data.get("your_name", "implenium")
    basic_context = get_basic_context_for_monster(monster_id)
    prompt = basic_context.format(color=color, your_name=your_name)
    return get_story_from_openai(prompt)
