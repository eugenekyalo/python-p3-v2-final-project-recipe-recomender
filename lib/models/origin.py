from ..db import CONN, CURSOR

class Origin:
    @classmethod
    def create(cls, name):
        CURSOR.execute('''
        INSERT INTO origins (name)
        VALUES (?)
        ''', (name,))
        CONN.commit()
        return CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS origins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute('SELECT * FROM origins')
        return CURSOR.fetchall()

    @classmethod
    def get_by_id(cls, origin_id):
        CURSOR.execute('SELECT * FROM origins WHERE id = ?', (origin_id,))
        return CURSOR.fetchone()

    @classmethod
    def update(cls, origin_id, name):
        CURSOR.execute('''
        UPDATE origins
        SET name = ?
        WHERE id = ?
        ''', (name, origin_id))
        CONN.commit()

    @classmethod
    def delete(cls, origin_id):
        CURSOR.execute('DELETE FROM origins WHERE id = ?', (origin_id,))
        CONN.commit()
