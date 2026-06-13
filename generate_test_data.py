import json
import os
from api.client import TandoorAPIClient


def generate_test_data():
    client = TandoorAPIClient()
    
    data_path = os.path.join(os.path.dirname(__file__), "data", "recipe_urls.json")
    with open(data_path, "r") as f:
        urls = json.load(f)["recipes"]
    
    recipe_ids = []
    for url in urls:
        try:
            response = client.import_recipe_by_url(url)
            recipe_id = response.get("id")
            recipe_ids.append(recipe_id)
            print(f"Imported recipe from {url}, ID: {recipe_id}")
        except Exception as e:
            print(f"Failed to import {url}: {e}")
    
    with open("data/recipe_ids.json", "w") as f:
        json.dump({"recipe_ids": recipe_ids}, f)
    
    print("Test data generation complete!")


if __name__ == "__main__":
    generate_test_data()