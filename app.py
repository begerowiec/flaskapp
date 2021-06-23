from flask import Flask, render_template, abort, make_response, request, redirect
import mysql.connector
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="guestbook"
)


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


@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        userform = request.form
        nick = userform['nick']
        tresc = userform['tekst']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO guests(nick,tekst) VALUES (%s, %s)", (nick, tresc))
        mydb.commit()
        mycursor.close()
        return redirect('/guestbook')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM guests ORDER BY data DESC")
    fetchdata = mycursor.fetchall()
    return render_template('guestbook.html', allposts=fetchdata)


@app.route('/error_denied')
def error_denied():
    abort(401)


@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
