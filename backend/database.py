# Function to get a database connection
import pyodbc

# LocalDB connection string
connection_string = """
    DRIVER={ODBC Driver 18 for SQL Server};
    SERVER=(localdb)\kris_local_db;
    DATABASE=FastApiVueApp;
    Trusted_Connection=yes;
"""

# Function to get a database connection
def get_db():
    try:
        conn = pyodbc.connect(connection_string)
        print("✅ Successfully connected to the database!")
        return conn
    except pyodbc.Error as e:
        print("❌ Failed to connect to the database:", e)
        raise

if __name__ == "__main__":
    conn = get_db()
    cursor = conn.cursor()

    # Verify the database name
    cursor.execute("SELECT DB_NAME()")
    db_name = cursor.fetchone()[0]
    print(f"Connected to database: {db_name}")

    # cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", ('Test Item', 'Test Description'))
    # conn.commit()

    # cursor.execute("SELECT * FROM items")
    # print(cursor.fetchall())
    # cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'items'")
    # table_exists = cursor.fetchone()
    # if table_exists:
    #     print("✅ Table 'items' exists.")
    # else:
    #     print("❌ Table 'items' does not exist.")
    # # Check if there are any records in the table
    # cursor.execute("SELECT COUNT(*) FROM items")
    # record_count = cursor.fetchone()[0]
    # print(f"Number of records in 'items' table: {record_count}")


    #     # Fetch all records from the table
    # cursor.execute("SELECT * FROM items")
    # result = cursor.fetchall()
    # print("Records in 'items' table:", result)