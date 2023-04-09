from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "key secret"

@app.route('/')
def dojo_survery():
    return render_template("/dojo_survey.html")

@app.route('/get_data', methods=['POST'])
def get_data():
    # Store Form Data
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/display_data')

@app.route('/display_data')
def display_data():
    # Display Form Data
    return render_template('/display_data.html')

@app.route('/reset_info')
def reset_info():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)