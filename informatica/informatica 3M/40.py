from flask import Flask, render_template
import json

app = Flask(__name__)

def read_recipes(filename: str) -> None:
    with open(filename) as f:
        data = json.load(f)
    for recipe in data:
        print(f"ID: {recipe['id']}")
        print(f"Name: {recipe['name']}")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Instructions: {recipe['instructions']}")
        print()

def get_recipe_by_id(id: int) -> None:
    with open('recipes.json') as f:
        data = json.load(f)
    for recipe in data:
        if recipe['id'] == id:
            print(f"ID: {recipe['id']}")
            print(f"Name: {recipe['name']}")
            print(f"Ingredients: {recipe['ingredients']}")
            print(f"Instructions: {recipe['instructions']}")
            return

def prompt_for_id() -> int:
    id = int(input("Inserisci l'ID della ricetta che vuoi vedere: "))
    return id

def get_all_recipes() -> list:
    with open('recipes.json') as f:
        data = json.load(f)
    return data

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = get_recipe_by_id(id)
    return render_template('recipe.html', recipe=recipe)

@app.route('/recipes')
def recipes():
    all_recipes = get_all_recipes()
    return render_template('recipes.html', recipes=all_recipes)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
