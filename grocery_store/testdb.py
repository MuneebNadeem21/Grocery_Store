import pyodbc

def test_db_connection():
    conn = None
    try:
        # Using Windows Authentication (Trusted Connection)
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'  # Use your actual server name or IP
            'DATABASE=Grocert_Store;'  # Use your actual database name
            'Trusted_Connection=yes;'  # Enable Windows Authentication
        )
        print("Database connection successful!")
    except Exception as e:
        print("Error: Unable to connect to the database.")
        print(e)
    finally:
        if conn:
            conn.close()

test_db_connection()
