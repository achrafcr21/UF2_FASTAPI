from database import db_connection
import random

# ------------------ Funcions per a "users" ------------------
def create_user(user_data: dict):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                           (user_data["name"], user_data["email"], user_data["password"]))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()
    return False

def get_user(user_id: int):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    return None

def update_user(user_id: int, user_data: dict):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s", 
                           (user_data["name"], user_data["email"], user_data["password"], user_id))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()
    return False

def delete_user(user_id: int):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()
    return False

# ------------------ Funcions per a "word" ------------------
def create_word(word_data: dict):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO word (word, theme) VALUES (%s, %s)", 
                           (word_data["word"], word_data["theme"]))
            conn.commit()
            return True
        except:
            return False
        finally:
            cursor.close()
            conn.close()
    return False

def get_word():
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM word")
        words = cursor.fetchall()
        cursor.close()
        conn.close()
        return random.choice(words)[0] if words else None
    return None

# ------------------ Funcions per a "alphabet" ------------------
def get_alphabet_by_language(lang: str):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT letter FROM alphabet WHERE lang = %s", (lang,))
        letters = cursor.fetchall()
        cursor.close()
        conn.close()
        return [letter[0] for letter in letters]
    return None