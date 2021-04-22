# -*- coding: utf-8 -*-
from flask import Flask, request
import os
import json

from CookIT.searcher import Searcher

app = Flask(__name__)

fridge = {}
fridge_en = []  # For caching
fridge_ru = []
fridge_json = ""

try:
    with open('./CookIT/fridge.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            fridge_en.append(line.strip())
    with open('./CookIT/fridge_ru.txt', 'r', encoding='utf8') as f:
        for line in f.readlines():
            fridge_ru.append(line.strip())
    for i, item in enumerate(fridge_en):
        fridge[item] = fridge_ru[i].capitalize()
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


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == "__main__":
    app.run()
