# app.py - Your Flask application
from flask import Flask
import os

app = Flask(__name__)
counter_file = '/app/counter.txt'

@app.route('/')
def get_counter():
    current_count = 1
    if os.path.exists(counter_file):
        with open(counter_file, 'r') as f:
            current_count = int(f.read())
            current_count += 1
    with open(counter_file, 'w') as f:
        f.write(str(current_count))
    return f'Hello! You are visitor number {current_count}.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
