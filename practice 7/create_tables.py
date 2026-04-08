from connect import connect

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            contact_id SERIAL PRIMARY KEY,
            contact_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(20) NOT NULL UNIQUE
        )
        """,
    )
    conn = None
    try:
        conn = connect()
        if conn:
            cur = conn.cursor()
            for command in commands:
                cur.execute(command)
            cur.close()
            conn.commit()
            print("Кесте сәтті жасалды.")
    except Exception as e:
        print(f"Кесте жасау қатесі: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_tables()