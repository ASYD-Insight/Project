from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/scrape', methods=['GET'])
def get_data():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()

    data = []
    for row in rows:
        if len(row) == 5:
            item = {
                'id': row[0],
                'Title': row[1],
                'Link': row[2],
                'Price': row[3],
                'Stock': row[4]
            }
            data.append(item)
        else:
            print("Row does not have 5 columns:", row)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
