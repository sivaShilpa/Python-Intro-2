import psycopg2

DB_NAME = "vnpeeabt"
DB_USER = "vnpeeabt"
DB_PASS = "bhjebMEOe5H-2nBZYhw-8qZ_-e611Evn"
DB_HOST = "suleiman.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                        host=DB_HOST, port=DB_PORT)
print("Database connected successfully.")

cur = conn.cursor()
cur.execute("""
CREATE TABLE Cat 
(
CAT_ID INTEGER PRIMARY KEY NOT NULL, 
CAT_NAME TEXT NOT NULL,
STATUS TEXT NOT NULL
)
""")

conn.commit()

print("Table created successfully.")