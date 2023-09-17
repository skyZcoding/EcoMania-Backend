from score_request.get_sustainability_score import ratings


def get_popular_products(n_products=50):
    """Get the most popular products from the ratings dataframe."""
    products = ratings[['ID', 'Name', 'Popularity', 'Price', 'image', 'Cargo']]
    products = products.sort_values('Popularity', ascending=False)
    popular_products = products[:n_products]
    product_json = popular_products.to_json(orient='records')
    return product_json

def get_demo_products(n_products=50):
    """Get products that have a variety of ratings."""
    base = 100
    products = ratings[['ID', 'Name', 'Popularity', 'Price', 'image', 'Cargo']]
    products = products.sort_values('Popularity', ascending=False)
    products.dropna(subset=['Cargo', 'Price'], inplace=True)
    products = products[base:base + n_products]
    product_json = products.to_json(orient='records')
    return product_json
