import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

def create_connection():
    try:
        db_file = 'recipe.db'  # Adjust if you need to use a different path
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to SQLite database at {db_file}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to SQLite database: {e}")
        return None

def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                instructions TEXT,
                cuisine TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                quantity INTEGER,
                unit TEXT,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dietary_restrictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe_dietary_restrictions (
                recipe_id INTEGER NOT NULL,
                restriction_id INTEGER NOT NULL,
                FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                FOREIGN KEY (restriction_id) REFERENCES dietary_restrictions(id),
                PRIMARY KEY (recipe_id, restriction_id)
            )
        """)

        conn.commit()
        logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")

def insert_sample_data(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO recipes (title, instructions, cuisine)
            VALUES ('Spaghetti Carbonara', 'Boil pasta. Cook pancetta. Mix with eggs and cheese.', 'Italian')
        """)

        cursor.execute("""
            INSERT INTO ingredients (recipe_id, name, quantity, unit)
            VALUES (1, 'Spaghetti', 200, 'grams'),
                   (1, 'Pancetta', 150, 'grams'),
                   (1, 'Eggs', 2, 'pieces'),
                   (1, 'Parmesan cheese', 50, 'grams')
        """)

        cursor.execute("""
            INSERT INTO dietary_restrictions (name)
            VALUES ('Vegetarian'), ('Gluten-free'), ('Nut-free')
        """)

        cursor.execute("""
            INSERT INTO recipe_dietary_restrictions (recipe_id, restriction_id)
            VALUES (1, 1), (1, 2)  -- Assuming recipe 1 is associated with dietary restrictions 1 and 2
        """)

        conn.commit()
        logging.info("Sample data inserted successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error inserting sample data: {e}")

def close_connection(conn):
    if conn:
        conn.close()
        logging.info("SQLite connection closed.")

if __name__ == "__main__":
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        insert_sample_data(conn)  # Call insert_sample_data to insert sample data
        close_connection(conn)
    else:
        logging.error("Failed to create database connection.")
