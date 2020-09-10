import psycopg2


def connection():
    global conn 
    conn = psycopg2.connect("dbname='books' user='postgres' password='admin' host='localhost' port='5432'")
    print("connection is successful")
    return conn


def create_table():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mybooks(id SERIAL PRIMARY KEY NOT NULL,title VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL,rating REAL,finished DATE,opinion TEXT)")
    conn.commit()
    conn.close()

def add_book(title,author,rating,finished,opinion):
    cur = conn.cursor()
    cur.execute("INSERT INTO mybooks(title,author,rating,finished,opinion) VALUES(%s,%s,%s,%s,%s) ",(title,author,rating,finished,opinion))
    conn.commit()
    conn.close()


def view():
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybooks")
    rows = cur.fetchall()
    conn.close()
    return rows





connection()

add_book('testgfhf','test',5,'10/09/2020','test')