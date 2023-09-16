import os
import numpy as np
import pandas as pd
from typing import List

ratings = pd.read_csv(os.path.join(os.path.dirname(__file__), "ratings.csv"))
SUSTAINABILITY_THRESHOLD = 3.5

def get_sustainability_score(products_list: List[int]):
    print(f"INFO - get_sustainability_score got products {products_list}")
    ids = set(products_list)
    score = np.mean([ratings[ratings["ID"] == id]["Cargo"].values[0] for id in ids])
    return {
        "sustainable": score >= SUSTAINABILITY_THRESHOLD,
        "score": score
    }
