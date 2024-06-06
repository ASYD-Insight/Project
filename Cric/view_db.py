import sqlite3

def fetch_data():
    try:
        conn = sqlite3.connect('predictions.db')
        cursor = conn.cursor()

        # Check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='prediction'")
        table_exists = cursor.fetchone()
        if not table_exists:
            print("The 'prediction' table does not exist.")
            return

        # Fetch data from the table
        cursor.execute("SELECT * FROM prediction")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        conn.close()
    except sqlite3.Error as e:
        print("SQLite error:", e)

if __name__ == "__main__":
    fetch_data()
