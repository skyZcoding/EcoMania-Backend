import os


def get_basic_context_for_monster(monster_id):
    match monster_id:

        case 1:
            # This is the bird
            file_path = os.path.join(os.path.dirname(__file__), "stories", '1_bird_story.txt')

        case _:
            print(f"ERROR! NO MONSTER WITH ID {monster_id}")
            file_path = os.path.join(os.path.dirname(__file__),"stories", 'default_story.txt')

    with open(file_path) as f:
        basic_context = f.read()

    return basic_context
