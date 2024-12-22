from flask import Flask, jsonify
import json

app = Flask(__name__)

# Функция для загрузки данных из JSON-файла
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/courses', methods=['GET'])
def get_courses():
    data = load_data()
    return jsonify(data['courses'])

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses', methods=['GET'])
def get_courses():
    data = load_data()
    return jsonify(data['courses'])

if __name__ == '__main__':
    app.run(debug=True)