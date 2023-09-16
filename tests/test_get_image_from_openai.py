import unittest

from image_request.get_image import get_image_api
from image_request.openai_img_utils import get_image_from_openai
from story_request.get_story import get_story_api


class TestGetImageOpenai(unittest.TestCase):

    def test_dummy(self):
        monster_data = {
            "monster_id": 0,
            "color": "white"
        }
        image = get_image_api(monster_data)
        print(image)
