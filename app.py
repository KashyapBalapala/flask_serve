from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return "about page"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        name = request.form['name']
        message = request.form['message']
        return f"Received: Name - {name}, Message - {message}"
    return render_template('form.html')


# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     message = request.form['message']
#     return f"Received: Name - {name}, Message - {message}"

if __name__ == '__main__':
    app.run(debug=True)
