from flask import Flask
from flask import render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/galleryold')
def galleryold():
    return render_template('galleryold.html')


if __name__ == '__main__':
    app.run(debug=True)