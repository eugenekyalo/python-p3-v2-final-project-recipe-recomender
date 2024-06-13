import sqlite3

# Connect to the database (assuming connection is established in db.py)
conn, cursor = create_connection()  # Import create_connection from db.py


class DietaryRestriction:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        cursor.execute("""
            INSERT INTO dietary_restrictions (name) VALUES (?)
        """, (name,))
        conn.commit()
        cursor.execute("SELECT last_insert_rowid()")
        id = cursor.fetchone()[0]
        return cls(id, name)

    @classmethod
    def get_by_id(cls, restriction_id):
        cursor.execute(f"SELECT * FROM dietary_restrictions WHERE id = {restriction_id}")
        row = cursor.fetchone()
        if row:
            return cls(*row)  # Unpack row data into constructor arguments
        return None

    def update(self, name):
        cursor.execute(f"UPDATE dietary_restrictions SET name = ? WHERE id = {self.id}", (name,))
        conn.commit()

    def delete(self):
        cursor.execute(f"DELETE FROM dietary_restrictions WHERE id = {self.id}")
        conn.commit()
