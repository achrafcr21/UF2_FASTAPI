import psycopg2 as pg

def db_connection():

    conn = pg.connect(
        database="postgres",
        user="user_postgres",
        password="pass_postgres",
        host="localhost",
        port="5432",
    )
    return conn
    # try:


       
    # except Exception as e:
    #     print(f"No s'ha pogut connectar a la base de dades: {e}")
    #     return None