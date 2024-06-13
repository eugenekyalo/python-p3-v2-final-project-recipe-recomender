from db import create_connection, create_tables
from models.recipe import Recipe

def populate_data(conn):
    # Create sample recipes
    recipe1 = Recipe(conn, "Spaghetti Bolognese", "Boil spaghetti. Cook minced meat with tomatoes and spices.", "Italian")
    recipe1.save()

    recipe2 = Recipe(conn, "Vegan Tacos", "Prepare taco shells. Fill with beans, corn, avocado, and vegan cheese.", "Mexican")
    recipe2.save()

    # Optionally add more recipes here...

    print("Database populated with sample data.")

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    populate_data(conn)
    conn.close()
