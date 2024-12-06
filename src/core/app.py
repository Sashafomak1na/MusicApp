from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the Music App!'


@app.route('/tracks')
def tracks():
    conn = sqlite3.connect('music_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tracks')
    tracks = cursor.fetchall()
    conn.close()
    return render_template('tracks.html', tracks=tracks)


if __name__ == '__main__':
    app.run(debug=True)