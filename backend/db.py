import os
import mysql.connector

# Load MySQL connection details from Railway environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "cablelist")

# Connect to MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Initialize database & create tables
def init_db():
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
