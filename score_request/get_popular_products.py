import json

import pandas as pd

from score_request.get_sustainability_score import ratings


def get_popular_products(n_products=50):
    products = ratings[['ID', 'Name', 'Popularity', 'Price', 'image', 'Cargo']]
    products = products.sort_values('Popularity', ascending=False)
    popular_products = products[:n_products]
    product_json = popular_products.to_json(orient='records')
    return product_json
