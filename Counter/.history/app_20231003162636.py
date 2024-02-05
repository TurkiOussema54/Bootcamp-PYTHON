from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    # Initialize the session variable if it doesn't exist
    if 'counter' not in session:
        session['counter'] = 0
    
    # Increment the counter by the specified amount (default is 0)
    increment = request.args.get('increment', default=0, type=int)
    session['counter'] += increment
    
    # Get the number of times the client has visited this site
    visit_count = session.get('visit_count', 0)
    
    return render_template('index.html', counter=session['counter'], visit_count=visit_count)

@app.route('/destroy_session')
def destroy_session():
    # Clear the session and redirect to the root route
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment_counter/<int:amount>')
def increment_counter(amount):
    # Increment the counter by the specified amount
    if 'counter' in session:
        session['counter'] += amount
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
