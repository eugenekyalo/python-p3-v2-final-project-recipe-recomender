import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Function to create a connection to the SQLite database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to SQLite database at {db_file}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to SQLite database: {e}")
        return None

# Function to add a new recipe to the database
def add_recipe(conn, title, instructions, cuisine):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO recipes (title, instructions, cuisine)
            VALUES (?, ?, ?)
        """, (title, instructions, cuisine))
        conn.commit()
        logging.info(f"Recipe '{title}' added successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error adding recipe: {e}")

# Function to list all recipes in the database
def list_recipes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes")
        rows = cursor.fetchall()
        logging.info("Listing all recipes:")
        for row in rows:
            logging.info(f"ID: {row[0]}, Title: {row[1]}, Cuisine: {row[3]}")
    except sqlite3.Error as e:
        logging.error(f"Error listing recipes: {e}")

# Function to query recipes based on cuisine
def query_recipes_by_cuisine(conn, cuisine):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes WHERE cuisine=?", (cuisine,))
        rows = cursor.fetchall()
        logging.info(f"Recipes with cuisine '{cuisine}':")
        for row in rows:
            logging.info(f"ID: {row[0]}, Title: {row[1]}, Cuisine: {row[3]}")
    except sqlite3.Error as e:
        logging.error(f"Error querying recipes: {e}")

# Function to close the database connection
def close_connection(conn):
    if conn:
        conn.close()
        logging.info("SQLite connection closed.")

# Main CLI interface
def main():
    db_file = 'recipe.db'  # Adjust if needed
    conn = create_connection(db_file)
    if conn is None:
        logging.error("Failed to connect to the database.")
        return

    # Example usage of CLI functions
    add_recipe(conn, "Spaghetti Carbonara", "Boil pasta. Cook pancetta. Mix with eggs and cheese.", "Italian")
    list_recipes(conn)
    query_recipes_by_cuisine(conn, "Italian")

    close_connection(conn)

if __name__ == "__main__":
    main()
