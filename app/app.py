from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def print_environment():
    env_vars = '</br>'.join([f'{key}: {value}' for key, value in os.environ.items()])
    return f'<h1>Environment Variables</h1><p>{env_vars}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
