from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')
def render_form():
    return render_template('generate.html')

@app.route('/result', methods=['POST'])
def show_result():
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    sex = request.form['sex']
    institution = request.form['institution']
    email = request.form['email']

    return render_template(
        'result.html',
        lastname=lastname,
        firstname=firstname,
        sex=sex,
        institution=institution,
        email=email
    )

if __name__ == '__main__':
    app.run(debug=True)
