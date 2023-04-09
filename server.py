from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "key secret"

@app.route('/')
def dojo_survery():
    return redirect("/dojo_survery.html")

if __name__ == "__main__":
    app.run(debut = True)