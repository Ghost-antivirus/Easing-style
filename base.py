from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('commands.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS commands
             (ip TEXT, command TEXT)''')

@app.route('/send_command', methods=['POST'])
def send_command():
    ip = request.form['ip']
    command = request.form['command']
    c.execute("INSERT INTO commands (ip, command) VALUES (?, ?)", (ip, command))
    conn.commit()
    return 'Command sent'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)