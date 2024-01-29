import sqlite3

def create_users_table(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create the users table
        cursor.execute('''
            CREATE TABLE Users (
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                First_name VARCHAR(255) NOT NULL,
                Last_name VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL UNIQUE,
                Role VARCHAR(50) NOT NULL DEFAULT 'user' -- Default role is set to 'user'
            );
        ''')

        # Commit the changes (creating the table)
        conn.commit()
        print("Table 'users' created successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection, whether an exception occurred or not
        if conn:
            conn.close()

# Specify the name of your SQLite database file
db_file = "database.db"

# Call the function to create the 'Users' table
create_users_table(db_file)