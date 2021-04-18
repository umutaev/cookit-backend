# -*- coding: utf-8 -*-
from flask import Flask, request
import os
import json

from CookIT.searcher import Searcher

app = Flask(__name__)

fridge = []  # For caching
fridge_json = ""

try:
    with open('./CookIT/fridge.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            fridge.append(line.strip())
        fridge_json = json.dumps(fridge)
except FileNotFoundError:
    exit(os.EX_NOTFOUND)

liked_recipes = []


@app.route('/get_ingredients')
def get_ingredients():
    return fridge_json


@app.route('/generate', methods=['POST'])
def generate_recipe():
    user_fridge = request.get_json()['ingredients']
    neural_recipes = Searcher(user_fridge).get_suitable_recipes(language='ru')
    return json.dumps(neural_recipes, ensure_ascii=False).encode('utf8').decode('utf8')


if __name__ == "__main__":
    app.run()
