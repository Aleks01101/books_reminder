import psycopg2


try:
    conn = psycopg2.connect("dbname='books' user='postgres' password='admin' host='localhost' port='5432'")
    print("Data base connected successfully")
except(Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)




def create_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mybooks(id SERIAL PRIMARY KEY NOT NULL,title VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL,rating REAL,finished DATE,opinion TEXT)")
    conn.commit()
    conn.close()

def add_book(title,author,rating,finished,opinion):
    cur = conn.cursor()
    cur.execute("INSERT INTO mybooks(title,author,rating,finished,opinion) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (title) DO NOTHING ",(title,author,rating,finished,opinion))
    conn.commit()
    conn.close()


def view():
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybooks")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    cur = conn.cursor()
    cur.execute("DELETE FROM mybooks WHERE item=%s"),(item)
    conn.commit()
    conn.close()

def update(rating,finished,opinion,title,author):
    cur = conn.cursor()
    cur.execute("UPDATE mybooks SET rating=%s, finished=%s, opinion=%s WHERE title=%s, author=%s "),(rating,finished,opinion,title,author)
    conn.commit()
    conn.close()


add_book('testgfhf','test',5,'10/09/2020','test')