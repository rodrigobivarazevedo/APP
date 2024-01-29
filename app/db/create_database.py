import sqlite3  

def create_database(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        print("SQLite version:", sqlite3.version)

        # Commit the changes (in this case, creating the database)
        conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection, whether an exception occurred or not
        if conn:
            conn.close()

create_database("database.db")