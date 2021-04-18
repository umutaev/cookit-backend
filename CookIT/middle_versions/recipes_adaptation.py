import json
recipes_dictionary={}
fridge_list=[]
with open("fridge.txt") as fridge:
    for food_name in fridge.readlines():
        fridge_list.append(food_name.strip())
with open("sort_later.txt", "w") as garbage:
    with open("recipes_raw_nosource_fn.json") as json_file:
        data = json.load(json_file)
        for recipe in data:
            try:
                ingredients_raw = data[recipe]["ingredients"]
                ingredients_mask = ["0" for i in range(len(fridge_list))]
                for product in ingredients_raw:
                    flag=1
                    for abstraction_index in range(len(fridge_list)):
                        if fridge_list[abstraction_index] in product.lower():
                            ingredients_mask[abstraction_index]="1"
                            flag=0
                            break
                    if flag:
                        try:
                            garbage.write(product+"\n")
                        except UnicodeEncodeError:
                            print(product)

                bin_recipe=int(''.join(ingredients_mask), 2)
                recipes_dictionary[recipe]=bin_recipe
            except KeyError:
                pass

print(len(recipes_dictionary))
# print(recipes_dictionary)

with open('adapted_recipes.json', 'w') as fp:
    json.dump(recipes_dictionary, fp)
