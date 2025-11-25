from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/nft')
def nft():
    return render_template('nft.html')


@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
