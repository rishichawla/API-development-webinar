from flask import Flask, render_template, redirect
import requests
import json

app = Flask(__name__)

url = 'https://api.covid19api.com/'

@app.route('/', methods=["GET"])
def getStats():
    response = requests.get(url+'summary')
    response = json.loads(response.text)
    return render_template('index.html', countries=response['Countries'][1:11])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)