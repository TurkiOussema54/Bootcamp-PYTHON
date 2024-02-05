from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
visit_count = 0  # Initialize the visit count

@app.route('/')
def index():
    global visit_count  # Use the global visit_count variable
    visit_count += 1  # Increment the visit count each time the root route is viewed
    return render_template('index.html', visit_count=visit_count)

@app.route('/destroy_session')
def destroy_session():
    global visit_count  # Use the global visit_count variable
    visit_count = 0  # Reset the visit count
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
