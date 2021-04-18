ingredients=[]
with open("my_ings_2.txt", "w") as dump_file:
    with open("my_ing_list.txt", "r") as source:
        for i in source.readlines():
            new_ing = i.strip()
            if ingredients and (new_ing==ingredients[-1]+"s" or new_ing==ingredients[-1]+"es"):
                pass
            else:
                ingredients.append(new_ing)
                dump_file.write(new_ing+"\n")
print(ingredients)

