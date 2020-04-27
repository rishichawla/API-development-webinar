from flask import Flask, render_template, request, jsonify, redirect
import json
import psycopg2

app = Flask(__name__)

def generateUsers(n):
    from randomuser import RandomUser
    
    users = {"abc": "123"}
    temp = RandomUser.generate_users(5)

    for user in temp:
        users[user.get_username()] = user.get_password()

    with open('users.json', 'w') as outfile:
        json.dump(users, outfile, indent=2)

def config(filename='database.ini', section='postgresql'):
    from configparser import ConfigParser

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

params = config()

def checkLogin(username, password):
    try:
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)

        cur = connection.cursor()
        cur.execute('SELECT password from login where username = %s', (username,))

        row = cur.fetchone()

        if row is None:
            return False
        
        if password == row[0]:
            return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return False

@app.route('/')
def main():
    return 'Hello World'

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if checkLogin(request.form['username'], request.form['pass']):
            return redirect('http://localhost:5001/')
    return render_template('index.html')

if __name__ == '__main__':
    generateUsers(5)

    app.run(host='0.0.0.0', port=5000, debug=True)