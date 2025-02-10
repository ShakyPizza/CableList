import os
import mysql.connector

# Load MySQL connection details from Railway environment variables
DB_HOST = os.getenv("DB_HOST", "mysql.railway.internal")  # Update this!
DB_PORT = os.getenv("DB_PORT", 18658)  # Use Railway's MySQL port
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "IPWOPapVndgFeqvKqAXwRoAlpGwMbMtj")  # Update this!
DB_NAME = os.getenv("DB_NAME", "railway")

def get_db_connection():
    """Connect to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=int(DB_PORT),
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database Connection Error: {err}")
        return None

def init_db():
    """Initialize the MySQL database."""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cables (
                id INT AUTO_INCREMENT PRIMARY KEY,
                column1 VARCHAR(255),
                column2 VARCHAR(255),
                column3 VARCHAR(255),
                column4 VARCHAR(255)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()
