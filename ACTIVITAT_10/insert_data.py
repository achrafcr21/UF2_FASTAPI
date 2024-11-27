import pandas as pd
from database import db_connection


# Llegeix les dades del CSV i insereix-les a la base de dades
def insert_data_from_csv(file_path):
    try:
        # Llegeix el CSV
        df = pd.read_csv(file_path)

        # Connexió a la DB
        conn = db_connection()
        if not conn:
            return

        cursor = conn.cursor()

        # Inserció de dades a la taula `words`
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO words (word, theme) VALUES (%s, %s)",
                (row['WORD'], row['THEME'])
            )

        conn.commit()
        cursor.close()
        conn.close()

        print("Dades inserides correctament.")
    except Exception as e:
        print(f"Error inserint dades: {e}")

# Executa l'script
if __name__ == "__main__":
    insert_data_from_csv("ACTIVITAT_10\paraules_temàtica_penjat.csv")