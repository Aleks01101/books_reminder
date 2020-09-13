import psycopg2


# try:
#     conn = psycopg2.connect("dbname='books' user='postgres' password='admin' host='localhost' port='5432'")
#     print("Data base connected successfully")
# except(Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL", error)



def connection():
    global conn
    conn = psycopg2.connect("dbname='books' user='postgres' password='admin' host='localhost' port='5432'")
    # print("Data base connected successfully")

def create_table():
    connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mybooks(id SERIAL PRIMARY KEY NOT NULL,title VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL,rating FLOAT,finished DATE,opinion TEXT)")
    conn.commit()
    conn.close()

def add_book(title,author,rating,finished,opinion):
    connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO mybooks(title,author,rating,finished,opinion) VALUES(%s,%s,%s,%s,%s)",(title,author,rating,finished,opinion))
    conn.commit()
    conn.close()


def view():
    connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybooks")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM mybooks WHERE id=%s",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,rating,finished,opinion):
    connection()
    cur = conn.cursor()
    cur.execute("UPDATE mybooks SET title=%s, author=%s, rating=%s, finished=%s, opinion=%s WHERE id=%s ",(title,author,rating,finished,opinion,id))
    conn.commit()
    conn.close()



def search(title="",author=""):
    connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mybooks WHERE title=%s OR author=%s",(title,author))
    rows = cur.fetchall()
    conn.close()
    return rows
    

