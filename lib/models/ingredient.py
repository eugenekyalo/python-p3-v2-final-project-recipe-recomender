from ..db import CONN, CURSOR

class Ingredient:
    @classmethod
    def create(cls, name, nationality, vegan, calories, protein, carbohydrates, fats, recipe_id):
        CURSOR.execute('''
        INSERT INTO ingredients (name, nationality, vegan, calories, protein, carbohydrates, fats, recipe_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, nationality, vegan, calories, protein, carbohydrates, fats, recipe_id))
        CONN.commit()
        return CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nationality TEXT,
            vegan BOOLEAN,
            calories INTEGER,
            protein REAL,
            carbohydrates REAL,
            fats REAL,
            recipe_id INTEGER,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
        ''')
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM ingredients')
        return CURSOR.fetchall()

    @classmethod
    def get_by_id(cls, ingredient_id):
        CURSOR.execute('SELECT * FROM ingredients WHERE id = ?', (ingredient_id,))
        return CURSOR.fetchone()

    @classmethod
    def update(cls, ingredient_id, name, nationality, vegan, calories, protein, carbohydrates, fats, recipe_id):
        CURSOR.execute('''
        UPDATE ingredients
        SET name = ?, nationality = ?, vegan = ?, calories = ?, protein = ?, carbohydrates = ?, fats = ?, recipe_id = ?
        WHERE id = ?
        ''', (name, nationality, vegan, calories, protein, carbohydrates, fats, recipe_id, ingredient_id))
        CONN.commit()

    @classmethod
    def delete(cls, ingredient_id):
        CURSOR.execute('DELETE FROM ingredients WHERE id = ?', (ingredient_id,))
        CONN.commit()
