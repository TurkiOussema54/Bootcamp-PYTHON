from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random secret key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # Store form data in the session
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['favorite_color'] = request.form['favorite_color']

    return redirect("/result")

@app.route("/result")
def result():
    # Retrieve form data from session
    name = session.get('name')
    email = session.get('email')
    favorite_color = session.get('favorite_color')

    return render_template("result.html", name=name, email=email, favorite_color=favorite_color)

if __name__ == "__main__":
    app.run(debug=True)
