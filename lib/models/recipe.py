class Recipe:
    def __init__(self, conn, title, instructions, cuisine):
        self.conn = conn
        self.title = title
        self.instructions = instructions
        self.cuisine = cuisine
        self.id = None

    def save(self):
        cursor = self.conn.cursor()

        if self.id is None:
            # Inserting a new recipe
            cursor.execute('''
                INSERT INTO recipes (title, instructions, cuisine)
                VALUES (?, ?, ?)
            ''', (self.title, self.instructions, self.cuisine))
            self.conn.commit()
            self.id = cursor.lastrowid
        else:
            # Updating an existing recipe
            cursor.execute('''
                UPDATE recipes
                SET title = ?, instructions = ?, cuisine = ?
                WHERE id = ?
            ''', (self.title, self.instructions, self.cuisine, self.id))
            self.conn.commit()

        cursor.close()

    @classmethod
    def get_all(cls, conn):
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM recipes')
        recipes = cursor.fetchall()

        cursor.close()

        return recipes

    @classmethod
    def get_by_id(cls, conn, recipe_id):
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
        recipe = cursor.fetchone()

        cursor.close()

        return recipe

    @classmethod
    def delete(cls, conn, recipe_id):
        cursor = conn.cursor()

        cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
        conn.commit()

        cursor.close()
