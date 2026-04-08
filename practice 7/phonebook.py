import csv
from connect import connect

def insert_contact(name, phone):
    """Жаңа контакт қосу"""
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (contact_name, phone_number) VALUES (%s, %s)", (name, phone))
            conn.commit()
            print(f"{name} қосылды!")
        conn.close()

def get_all_contacts():
    """Барлық контактілерді көру"""
    conn = connect()    
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY contact_name")
            rows = cur.fetchall()
            print("\nКонтактілер тізімі:")
            for row in rows:
                print(f"{row[1]}: {row[2]}")
        conn.close()

# Тексеру үшін:
if __name__ == "__main__":
    # Бір контакт қосып көрейік
    name = input("Атын жазыңыз: ")
    phone = input("Нөмірін жазыңыз: ")
    insert_contact(name, phone)
    
    # Тізімді шығару
    get_all_contacts()
