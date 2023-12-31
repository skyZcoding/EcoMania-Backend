import os
from typing import List
import pandas as pd
import json

ratings = pd.read_csv(os.path.join(os.path.dirname(__file__), "ratings.csv"))
SUSTAINABILITY_THRESHOLD = 3.5


def get_sustainability_score(products_list: List[int]):
    print(f"INFO - get_sustainability_score got products {products_list}")
    ids = set(products_list)
    filtered_products = ratings[ratings['ID'].isin(ids)]
    if len(filtered_products):
        score = filtered_products["Cargo"].mean()
    else:
        print(f"ERROR! No products with ids {products_list}")
        score = 0

    return json.dumps({
        "sustainable": bool(score >= SUSTAINABILITY_THRESHOLD),
        "score": score
    })
