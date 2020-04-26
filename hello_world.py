from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/hello')
def hello():
    return '<h1><center>Hello World</center></h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)