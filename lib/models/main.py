# main.py

from db import engine, SessionLocal, Base
from models import Recipe, Ingredient, DietaryRestriction

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create a new recipe with ingredients and dietary restrictions
def create_recipe():
    new_recipe = Recipe.create(title="Pasta Carbonara", instructions="Boil pasta, mix with bacon and eggs", cuisine="Italian")

    # Add ingredients
    Ingredient.create(name="Pasta", nationality="Italian", vegan=False, recipe_id=new_recipe.id)
    Ingredient.create(name="Bacon", nationality="Various", vegan=False, recipe_id=new_recipe.id)

    # Add dietary restrictions
    DietaryRestriction.create(name="Non-Vegetarian")
    DietaryRestriction.create(name="High-Calorie")
    
    # Link dietary restrictions to the recipe
    new_recipe.restrictions.append(DietaryRestriction.get_by_id(1))  # Non-Vegetarian
    new_recipe.restrictions.append(DietaryRestriction.get_by_id(2))  # High-Calorie

    session = SessionLocal()
    session.add(new_recipe)
    session.commit()

# Retrieve and print a recipe with its ingredients and restrictions
def print_recipe(recipe_id):
    recipe = Recipe.get_by_id(recipe_id)
    if recipe:
        print(f"Recipe ID: {recipe.id}, Title: {recipe.title}, Cuisine: {recipe.cuisine}")
        print("Ingredients:")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient.name}, Nationality: {ingredient.nationality}, Vegan: {ingredient.vegan}")
        print("Dietary Restrictions:")
        for restriction in recipe.restrictions:
            print(f"- {restriction.name}")
    else:
        print("Recipe not found.")

if __name__ == "__main__":
    # Create a new recipe
    create_recipe()

    # Print the created recipe
    print_recipe(1)  # Assuming the newly created recipe has ID 1
