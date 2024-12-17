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


#funció per obtenir etadistiques del usuari

def get_registre_jugador(user_id: int):
    conn = db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT PPA, total_games, games_won, best_game
            FROM log_record
            WHERE user_id = %s
        """, (user_id,))
        registre = cursor.fetchone()
        cursor.close()
        conn.close()

        # Retorna les dades en format diccionari
        if registre:
            return {
                "ppa": registre[0],
                "total_games": registre[1],
                "games_won": registre[2],
                "best_game": registre[3]
            }
        else:
            return {}
    return {}