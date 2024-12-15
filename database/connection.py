# # import sqlite3

# # DATABASE_NAME = './database/magazine.db'

# # def get_db_connection():
# #     conn = sqlite3.connect(DATABASE_NAME)
# #     conn.row_factory = sqlite3.Row
# #     return conn


# import sqlite3

# DATABASE_NAME = './database/magazine.db'

# def get_db_connection():
#     try:
#         # Open a connection to the database
#         conn = sqlite3.connect(DATABASE_NAME)
        
#         # Enable foreign key support (this is important for foreign key constraints)
#         conn.execute('PRAGMA foreign_keys = ON')
        
#         # Enable row factory to return rows as dictionaries (access by column name)
#         conn.row_factory = sqlite3.Row
        
#         # Return the database connection object
#         return conn
#     except sqlite3.Error as e:
#         # Handle any SQLite-specific errors that occur during connection
#         print(f"Error connecting to the database: {e}")
#         return None



import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database and enables foreign key constraints.
    
    Returns:
        sqlite3.Connection: A connection object to the SQLite database if successful.
        None: If the connection fails due to any error.
    """
    try:
        # Open a connection to the SQLite database
        conn = sqlite3.connect(DATABASE_NAME)
        
        # Enable foreign key support (important for enforcing foreign key constraints)
        conn.execute('PRAGMA foreign_keys = ON')
        
        # Enable row factory to return rows as dictionaries (access by column name)
        conn.row_factory = sqlite3.Row
        
        return conn
    
    except sqlite3.Error as e:
        # Handle any SQLite-related errors (e.g., failure to connect)
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        # Handle any other general exceptions
        print(f"An unexpected error occurred: {e}")
    
    return None
