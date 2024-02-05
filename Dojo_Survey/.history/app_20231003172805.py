from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong, random secret key

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # Store form data in session
    session['your_name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']

    return redirect("/result")

@app.route("/result")
def result():
    # Retrieve form data from session
    name = session.get('your_name')
    email = session.get('location')
    favorite_color = session.get('favorite_language')

    return render_template("result.html", your_name=your_name, location=location, ffavorite_language=favorite_language)

@app.route("/comment", methods=["POST"])
def comment():
    user_comment = request.form['comment']
    
    # Store comments in a list in session
    if 'comments' not in session:
        session['comments'] = []
    session['comments'].append(user_comment)
    
    return redirect("/result")

if __name__ == "__main__":
    app.run(debug=True)
