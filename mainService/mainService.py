from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

url = 'https://api.covid19api.com/'

@app.route('/', methods=["GET"])
def getStats():
    response = requests.get(url+'summary')
    response = json.loads(response.text)
    return render_template('index.html', countries=response['Countries'][1:11])

@app.route('/country', methods=["GET"])
def getCountryStats():
    response = requests.get(url + 'total/country/' + request.args.get('country'))
    response = json.loads(response.text)

    confirmedCases = {}
    for data in response:
        confirmedCases[data['Date'][:10]] = data['Confirmed']


    return render_template('country.html', country = request.args.get('country'), confirmedCases = confirmedCases)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)