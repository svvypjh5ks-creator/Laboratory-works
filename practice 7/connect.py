import psycopg2
from config import load_config

def connect():
    """ PostgreSQL серверіне қосылу """
    try:
        params = load_config()
        print('Базаға қосылуда...')
        conn = psycopg2.connect(**params)
        
        print('Connected to the PostgreSQL server.')
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Қате шықты: {error}")

if __name__ == '__main__':
    connect()