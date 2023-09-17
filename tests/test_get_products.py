import json
import unittest
import numpy as np

from score_request.get_products import *


class TestGetPopularProducts(unittest.TestCase):

    def test_get_popular_products(self):
        n_products = 10
        results = get_popular_products(n_products=n_products)
        results = json.loads(results)
        self.assertEqual(len(results), n_products)

    def test_get_demo_products(self):
        n_products = 10
        results = get_demo_products(n_products=n_products)
        results = json.loads(results)
        std = np.std([r["Cargo"] for r in results if r["Cargo"] is not None])
        print("STANDARD DEVIATION", std)
        self.assertGreaterEqual(std, 1)