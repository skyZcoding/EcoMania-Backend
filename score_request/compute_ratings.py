import os
import json
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from argparse import ArgumentParser

def get_all_csvs(folder):
    """Collects all CSV files within the folder and returns a single pd.DataFrame"""
    data_frame = pd.DataFrame()
    for file in tqdm(os.listdir(folder), desc=f"Loading CSVs in {folder}"):
        if file.endswith(".csv"):
            shop = pd.read_csv(os.path.join(folder, file))
            data_frame = pd.concat([data_frame, shop])
    return data_frame

def get_all_jsons(folder):
    """Collects all JSON files within the folder and returns a single JSON"""
    return {
        fn[:-5] : json.load(open(os.path.join(folder, fn)))
        for fn in tqdm(
            [fn for fn in os.listdir(folder) 
            if fn.endswith(".json")],
            desc=f"Loading JSONs in {folder}"
        )
    }


def merge(args):
    """Merges infos from all dataset files"""
    data_path = args["data_path"]
    
    # Loading DataFrame with all transactions
    shops = get_all_csvs(os.path.join(data_path, "Shoppin_Cart"))
    
    # Loading JSON with all products
    products = get_all_jsons(os.path.join(data_path, "products", "en"))
    
    # Loading all sustainability scores
    sust_circ = pd.read_csv(os.path.join(data_path, "Dimension_circularity.csv"), sep=";", encoding='latin-1')
    sust_fish = pd.read_csv(os.path.join(data_path, "Fish_New.csv"), sep=";")
    sust_pack = pd.read_csv(os.path.join(data_path, "M-Check_packaging.csv"), sep=";", encoding='latin-1')
    
    # Computing popularity and sustainability of all products
    columns = ["ID", "Name", "Popularity", "Cargo", "Circularity", "Fish", "Packaging", "image", "image_transparent"]
    data_frame = pd.DataFrame(columns=columns)
    for product_id in tqdm(products, desc="Computing popularity and sustainability"):
        # Getting product name
        name = products[product_id]["name"]
        
        # Getting product popularity
        try:
            mask = (shops["ArtikelID"] == int(product_id))
            popularity = len(shops[mask]["KundeID"].unique())
        except:
            continue
        
        # Getting sustainability scores
        cargo, circ, fish, pack = np.NaN, np.NaN, np.NaN, np.NaN
        img, img_transp = None, None
        
        # Getting cargo rating
        try:
            cargo = products[product_id]["m_check2"]["carbon_footprint"]["ground_and_sea_cargo"]["rating"]
        except Exception:
            cargo = np.NaN

        # Getting product circularity score
        if product_id in sust_circ["Product_number"].values:
            circ = len(sust_circ[sust_circ["Product_number"] == product_id]["Product_circularity"].values[0])
        
        # Getting product fish score
        if product_id in sust_fish['Product_number'].values:
            fish = sust_fish[sust_fish['Product_number'] == product_id]["M-Check Fisch"].values[0]
    
        # Getting product packaging score
        if product_id in sust_pack["Product_number"].values:
            pack = sust_pack[sust_pack["Product_number"] == product_id]["M-Check Packaging"].values[0]
            
        # Getting product image
        try:
            img = products[product_id]["image"]["original"]
        except Exception:
            pass
        
        try:
            img_transp = products[product_id]["image_transparent"]["original"]
        except Exception:
            pass
        
        # Adding product to final dataframe
        data_frame.loc[int(product_id)] = [product_id, name, popularity, cargo, circ, fish, pack, img, img_transp]
    
    # Sorting dataframe by popularity
    data_frame = data_frame.sort_values(by="Popularity", ascending=False)
    
    # Storing the final dataframe
    data_frame.to_csv(os.path.join(data_path, "ratings.csv"), index=False)


def main(args):
    # Merging all data if not already done
    if not os.path.isfile(os.path.join(args["data_path"], "ratings.csv")):
        print("Merging all data...")
        merge(args)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data_path", type=str, default="./../Migros_case")
    args = vars(parser.parse_args())
    main(args)
