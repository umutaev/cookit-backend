import json
from fridge_util import Fridge
import pandas as pd
import numpy as np
fridge= Fridge()
fridge_list=fridge.product_list
correlation_matrix=np.zeros((fridge.volume, fridge.volume))
with open("recipes_raw_nosource_fn.json") as json_file:
    data = json.load(json_file)
    for recipe in data:
        try:
            ingredients_raw = data[recipe]["ingredients"]
            ingredient_set=set()
            for product in ingredients_raw:
                for abstraction_index in range(fridge.volume):
                    if fridge_list[abstraction_index] in product.lower():
                        ingredient_set.add(abstraction_index)
                        break
            for prod_a in ingredient_set:
                for prod_b in ingredient_set:
                    if prod_a!=prod_b:
                        correlation_matrix[prod_a][prod_b]+=1
                        correlation_matrix[prod_b][prod_a]+=1
                    else:
                        correlation_matrix[prod_a][prod_b]+=1

        except KeyError:
            pass
pd.DataFrame(correlation_matrix).to_csv("correlations.csv")
