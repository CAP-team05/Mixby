from collections import OrderedDict
import json

with open('api_codes/json_files/allIngredients.json', 'r', encoding='UTF-8') as json_read :
    all_ingredients = json.load(json_read, object_pairs_hook=OrderedDict)

def getCode(name):
    result = "None"
    for i in all_ingredients:
        if name == i["name"]:
            result = i["code"]
    return result