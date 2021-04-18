from searcher import Searcher

ingredients_i_have = ["garlic", "milk", "chicken", "pepper", "cabbage", "sugar", "cheese"]
for recipe in Searcher(ingredients_i_have).get_suitable_recipes(language="ru"):
    print(recipe["title"])
    print("Instructions:", recipe["instructions"])
    print("Ingredients:", recipe["ingredients"])

    print(("****************************\n"))
