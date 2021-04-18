import json
ing_set=set()
special_common_cases = ["milk", "oil", "flour", "sweetener", "sausages", "chicken", "peas", "ham", "cucumber", "liqueur", "whiskey"]
def add_ings(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        for i in data:
            ingredients = i['ingredients']
            for product in ingredients:
                # print(product.lower().split())
                result_ingredient=product
                for abstraction in special_common_cases:
                    if abstraction in product.lower().split():
                        result_ingredient=abstraction
                        break
                ing_set.add(result_ingredient)

add_ings("test.json")
add_ings("train.json")

print(len(ing_set))
print(ing_set)

with open("all_ingredients_list.txt", "w") as dump_file:
    for item in ing_set:
        dump_file.write(item+'\n')
