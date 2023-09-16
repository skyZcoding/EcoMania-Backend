import unittest

from story_request.get_story import get_story_api


class TestGetStoryOpenai(unittest.TestCase):

    def test_dummy(self):
        monster_data = {
            "monster_id": 0,
            "your_name": "ImpleniaDesigner",
            "color": "white"
        }
        story = get_story_api(monster_data)
        print(story)
