import unittest

from image_request.get_image import get_image_url_api


class TestGetImageOpenai(unittest.TestCase):

    def test_dummy(self):
        monster_data = {
            "monster_id": 0,
            "color": "white"
        }
        image = get_image_url_api(monster_data)
        print(image)
