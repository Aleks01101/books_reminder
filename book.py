import psycopg2


class Database:

    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname='books' user='postgres' password='admin' host='localhost' port='5432'")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS mybooks(id SERIAL PRIMARY KEY NOT NULL,title VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL,rating FLOAT,finished DATE,opinion TEXT)")
        self.conn.commit()
        print("Data base connected successfully")


    def add_book(self,title, author, rating, finished, opinion):
        self.cur.execute("INSERT INTO mybooks(title,author,rating,finished,opinion) VALUES(%s,%s,%s,%s,%s)",
                    (title, author, rating, finished, opinion))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM mybooks")
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM mybooks WHERE id=%s", (id,))
        self.conn.commit()

    def update(self,id, title, author, rating, finished, opinion):
        self.cur.execute("UPDATE mybooks SET title=%s, author=%s, rating=%s, finished=%s, opinion=%s WHERE id=%s ",
                    (title, author, rating, finished, opinion, id))
        self.conn.commit()

    def search(self,title="", author=""):
        self.cur.execute("SELECT * FROM mybooks WHERE title=%s OR author=%s",
                    (title, author))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()