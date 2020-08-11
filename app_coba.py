from flask import Flask, request 
import sqlite3
import pandas as pd 
app = Flask(__name__)

# data static 1 :
@app.route('/')
def test():
    conn = sqlite3.connect('data_input/chinook.db')
    tracks = pd.read_sql_query('SELECT * FROM invoices', conn)
    return tracks.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000) 