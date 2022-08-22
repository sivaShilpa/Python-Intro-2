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

cur.execute("INSERT INTO Cat (Cat_ID, Cat_Name, Status) VALUES(1, 'Gypsy', 'Hungry')")
conn.commit()

print("Data inserted successfully.")

conn.close()

