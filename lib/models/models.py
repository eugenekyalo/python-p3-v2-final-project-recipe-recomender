import sqlite3

# Connect to the database (assuming connection is established in db.py)
conn, cursor = create_connection()


class Recipe:
    def __init__(self, id, title, instructions, cuisine):
        self.id = id
        self.title = title
        self.instructions = instructions
        self.cuisine = cuisine

    @classmethod
    def create(cls, title, instructions, cuisine):
        cursor.execute("""
            INSERT INTO recipes (title, instructions, cuisine) VALUES (?, ?, ?)
        """, (title, instructions, cuisine))
        conn.commit()
        # Get the newly created ID (optional)
        cursor.execute("SELECT last_insert_rowid()")
        id = cursor.fetchone()[0]
        return cls(id, title, instructions, cuisine)  # Return a new instance with ID

    @classmethod
    def get_by_id(cls, recipe_id):
        cursor.execute(f"SELECT * FROM recipes WHERE id = {recipe_id}")
        row = cursor.fetchone()
        if row:
            return cls(*row)  # Unpack row data into constructor arguments
        return None

    def update(self, title=None, instructions=None, cuisine=None):
        updates = []
        if title:
            updates.append(f"title = '{title}'")
        if instructions:
            updates.append(f"instructions = '{instructions}'")
        if cuisine:
            updates.append(f"cuisine = '{cuisine}'")

        if updates:
            update_str = ", ".join(updates)
            cursor.execute(f"UPDATE recipes SET {update_str} WHERE id = {self.id}")
            conn.commit()

    def delete(self):
        cursor.execute(f"DELETE FROM recipes WHERE id = {self.id}")
        conn.commit()


class Ingredient:
    def __init__(self, id, recipe_id, name, quantity, unit):
        self.id = id
        self.recipe_id = recipe_id
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @classmethod
    def create(cls, recipe_id, name, quantity, unit):
        cursor.execute("""
            INSERT INTO ingredients (recipe_id, name, quantity, unit) VALUES (?, ?, ?, ?)
        """, (recipe_id, name, quantity, unit))
        conn.commit()
        cursor.execute("SELECT last_insert_rowid()")
        id = cursor.fetchone()[0]
        return cls(id, recipe_id, name, quantity, unit)

    # Implement get_by_id, update, and delete methods similarly using
