from database import db_connection
import random

# Obté totes les temàtiques de la base de dades
def get_all_themes():
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT theme FROM words;")
            themes = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{"option": theme[0]} for theme in themes]
        except Exception as e:
            print(f"Error obtenint temàtiques: {e}")
            return []
    else:
        print("No s'ha pogut connectar a la base de dades.")
        return []

# Obté una paraula aleatòria segons la temàtica
def get_random_word_by_theme(theme):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT word FROM words WHERE theme = %s", (theme,))
            words = cursor.fetchall()
            cursor.close()
            conn.close()
            if words:
                return [{"option": random.choice(words)[0]}]  # Escull una paraula aleatòria
            return []
        except Exception as e:
            print(f"Error obtenint paraula per temàtica: {e}")
            return []
    else:
        print("No s'ha pogut connectar a la base de dades.")
        return []