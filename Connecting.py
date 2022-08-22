import psycopg2

DB_NAME = "vnpeeabt"
DB_USER = "vnpeeabt"
DB_PASS = "bhjebMEOe5H-2nBZYhw-8qZ_-e611Evn"
DB_HOST = "suleiman.db.elephantsql.com"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                               host=DB_HOST, port=DB_PORT)
    print("Database connected successfully.")
except:
    print("Database not connected.")
