import psycopg2 as pg

def db_connection():
    try:
        conn = pg.connect(
            database="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"No s'ha pogut connectar a la base de dades: {e}")
        return None

def read_users():
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, age FROM users;")
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{"id": u[0], "name": u[1], "email": u[2], "age": u[3]} for u in users]
        except Exception as e:
            print(f"Error llegint usuaris: {e}")
            return []