from ACTIVITAT_9.db_connect.database import db_connection

def read_users():
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, surname FROM users;")
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{"id": u[0], "name": u[1], "surname": u[2]} for u in users]
        except Exception as e:
            print(f"Error llegint usuaris: {e}")
            return []
    else:
        return []