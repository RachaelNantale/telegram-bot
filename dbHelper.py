import sqlite3


class DBHelper:
    print('creating table')
    def __init__(self, dbname='todo.sqlite'):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
        itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)" 
        ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (owner ASC)"
        self.connection.execute(tblstmt)
        self.connection.execute(itemidx)
        self.connection.execute(ownidx)
        self.connection.commit()
        

    def add_item(self, item_text, owner):
        sql = "INSERT INTO items (description, owner) VALUES (?, ?)"
        args = (item_text, owner)
        self.connection.execute(sql, args)
        self.connection.commit()

    def delete_item(self, item_text,owner):
        sql = "DELETE FROM items WHERE description = (?) AND owner = (?)"
        args = (item_text, owner)
        self.connection.execute(sql, args)
        self.connection.commit()

    def get_items(self, owner):
        sql = "SELECT description FROM items WHERE owner = (?)"
        args = (owner, )
        return [x[0] for x in self.connection.execute(sql, args)]