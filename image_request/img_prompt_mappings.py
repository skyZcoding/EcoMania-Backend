import os


def get_basic_prompt_for_monster_img(monster_id):
    match monster_id:

        case 1:
            # This is the bird
            file_path = os.path.join(os.path.dirname(__file__), "images_prompts", '1_bird_prompt.txt')

        case _:
            print(f"ERROR! NO MONSTER WITH ID {monster_id}")
            file_path = os.path.join(os.path.dirname(__file__), "images_prompts", 'default_prompt.txt.txt')

    with open(file_path) as f:
        basic_img_prompt = f.read()

    return basic_img_prompt
