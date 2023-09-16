import unittest

from score_request.get_sustainability_score import get_sustainability_score


class TestGetBasicContext(unittest.TestCase):

    def test_get_sustainability_score(self):
        # Sustainable items
        banana = 264200301000 # Rated 5
        carrot = 274502501000 # Rated 5
        strawberry = 265606703000 # Rated 5
        sustainable_basket = [banana, carrot, strawberry]
        
        # Not sustainable items
        smarties = 101341000000 # Rated 2
        meat = 220220085000 # Rated 1
        tortellini = 130181700000 # Rated 3
        not_sustainable_basket = [smarties, meat, tortellini]
        
        self.assertTrue(get_sustainability_score(sustainable_basket)["sustainable"])
        self.assertFalse(get_sustainability_score(not_sustainable_basket)["sustainable"])

    def test_get_sust_score_with_non_existent_ids(self):
        sustainable = get_sustainability_score([0, "ciao"])["sustainable"]
        self.assertEqual(0, sustainable)
