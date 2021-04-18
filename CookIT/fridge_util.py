class Fridge():
    def __init__(self):
        self.product_list = []
        with open("./CookIT/fridge.txt") as fridge:
            for food_name in fridge.readlines():
                self.product_list.append(food_name.strip())
        self.volume = len(self.product_list)

    def ings2mask(self, ings: list):
        mask = ["0" for i in range(self.volume)]
        for i in ings:
            try:
                ing_index = self.product_list.index(i)
                mask[ing_index] = "1"
            except:
                print("Wrong ingredient, can't find " + i)
        return int(''.join(mask), 2)

    def ings2indexes(self, ings:list):
        indexes=[]
        for i in ings:
            try:
                ing_index = self.product_list.index(i)
                indexes.append(ing_index)
            except:
                print("Wrong ingredient, can't find " + i)
        return indexes

    def indexes2ings(self, indexes:list):
        return [self.product_list[i] for i in indexes]
