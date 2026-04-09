from connect import get_connection

def search_contacts(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def add_or_update(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s,%s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def delete_contact(identifier):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (identifier,))

    conn.commit()
    cur.close()
    conn.close()


def get_page(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s,%s)", (limit, offset))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


if __name__ == "__main__":
    search_contacts("Ali")
    add_or_update("John", "777777777")
    get_page(5,0)
