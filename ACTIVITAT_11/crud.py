from database import db_connection
import random

# Funció per obtenir el botó "Començar partida"
def get_boto_comencar_partida():
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM word WHERE theme = 'general'")
        text = cursor.fetchone()
        cursor.close()
        conn.close()
        return text[0] if text else ""
    return ""

# Funció per obtenir intents incorrectes
def get_intents(log_id: int):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM attempt WHERE log_id = %s AND is_correct = false", (log_id,))
        intents = cursor.fetchone()
        cursor.close()
        conn.close()
        return intents[0]
    return 0

# Funció per obtenir l'alfabet segons idioma
def get_alfabet(lang: str):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT letter FROM alphabet WHERE lang = %s", (lang,))
        letters = cursor.fetchall()
        cursor.close()
        conn.close()
        return [row[0] for row in letters]
    return []

# Funció per obtenir una paraula aleatòria
def get_paraula_aleatoria():
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM word")
        paraules = cursor.fetchall()
        cursor.close()
        conn.close()
        return random.choice(paraules)[0] if paraules else ""
    return ""