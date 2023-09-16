import json
import unittest

from score_request.get_popular_products import get_popular_products


class TestGetPopularProducts(unittest.TestCase):

    def test_get_popular_products(self):
        n_products = 10
        results = get_popular_products(n_products=n_products)
        results = json.loads(results)
        for r in results:
            print(r)
        self.assertEqual(len(results), n_products)
