from flask import Flask, render_template, redirect, url_for
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'
names = ['denny', 'liran', 'james', 'beal', 'wilton']


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
        # check in dB in the website
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username
        return render_template('assignmnet9.html',
                               username=username, name=None)
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


if __name__ == '__main__':
    app.run()
