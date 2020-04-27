from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def generateUsers(n):
    from randomuser import RandomUser
    
    users = {"abc": "123"}
    temp = RandomUser.generate_users(5)

    for user in temp:
        users[user.get_username()] = user.get_password()

    with open('users.json', 'w') as outfile:
        json.dump(users, outfile, indent=2)

def checkLogin(username, password):
    f = open('users.json')

    data = json.load(f)

    if data[username] == password:
        return True    
    return False

@app.route('/')
def main():
    return 'Hello World'

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if checkLogin(request.form['username'], request.form['pass']):
            return render_template('welcome.html', name = request.form['username'])
    return render_template('index.html')


if __name__ == '__main__':
    generateUsers(5)

    app.run(host='0.0.0.0', port=5000, debug=True)