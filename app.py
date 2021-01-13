from flask import Flask, render_template, redirect, url_for
from flask import request, session
from flask import jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = '123'
names = ['denny', 'liran', 'james', 'beal', 'wilton']
counter = 0


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='bi_ex_mir')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # changes in db= commit
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # take all data that sumnu. list of uesrs
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@app.route('/users')
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    print(query_result)
    return render_template('assignment10.html', users=query_result)


@app.route('/assignment10', methods=['GET', 'POST'])
def assignment10():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    print(query_result)
    if request.method == 'POST':
        first_name = request.form['first_name']
        identify1 = request.form['id']
        print(identify1)
        query = "insert into users(identify1, first_name) VALUES ('%s', '%s')" % (identify1, first_name)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('assignment10.html', users=query_result)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args['identify1']
        query = "DELETE FROM USERS WHERE IDENTIFY1='%s'" % user_id
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return 'user deleted'


@app.route('/home')
def home():
    return render_template('resume.html')


@app.route('/my_contacts')
def contacts_function():
    return render_template('Contact.html')


@app.route('/Contact')
def get_contacts():
    return redirect(url_for('contacts_function'))


@app.route('/assignment8')
def assignment8():
    favour_num = 6
    return render_template('assignment8.html',
                           num=favour_num,
                           hobbies=['chess', 'swimming', 'running', 'cooking'],
                           music=['glgltz', 'pop', 'israeli songs'],
                           films=['netflix', 'coach carter'],
                           )


@app.route('/usingBlock')
def using():
    favour_num = 6
    return render_template('usingBlock.html',
                           num=favour_num,
                           hobbies=['chess', 'swimming', 'running', 'cooking'],
                           films=['netflix', 'coach carter'],
                           )


@app.route('/assignmnet9_h', methods=['GET', 'POST'])
def assign_9_func():
    return render_template('assignmnet9.html')


@app.route('/Contact_form')
def contact_name():
    if 'name' in request.args:
        name = request.args['name']
        return render_template('Contact.html', name=name)
    return render_template('Contact.html')


@app.route('/assignmnet9', methods=['GET', 'POST'])
def assign9_func():
    name = ''
    username = ''
    if request.method == 'POST':
        if not session['logged_in']:
            # check in dB in the website
            username = request.form['username']
            session['logged_in'] = True
            session['username'] = username
            return render_template('assignmnet9.html',
                                   username=username, name=None)
        else:
            session['logged_in'] = False
            username = None
            return render_template('assignmnet9.html',
                                   username=username, name=None, session_s=False)

    elif request.method == 'GET':
        name = request.args.get('nickname', None)
        if name in names:
            return render_template('assignmnet9.html',
                                   username=username, name=name)
        else:
            return render_template('assignmnet9.html',
                                   username=username, name=None)
    else:
        return render_template('assignmnet9.html',
                               username=username, name=None)


@app.route('/assignment11/users')
def get_users():
    if request.method == "GET":
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                'Error': 'There is no users data'
            })
        else:
            return jsonify({
                'success': 'True',
                'data': query_result

            })


@app.route('/assignment11/users/selected', defaults={'some_user_id': 3})
@app.route('/assignment11/users/selected/<int:some_user_id>', methods=['GET', 'POST'])
def get_user_by_id(some_user_id):
    if request.method == "GET":
        query = "Select * FROM users where identify1='%s'" % some_user_id
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                'Error': 'User doesnt exist'

            })
        else:
            return jsonify({
                'success': 'True',
                'data': query_result[0]
            })


if __name__ == '__main__':
    app.run()
