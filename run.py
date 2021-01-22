from flask import Flask, render_template, request, redirect
from data.db import add_new_contact
from time import time
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def my_home():
    """render home and index template"""
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    """reder and return the html template provided as page_name"""
    return render_template(page_name)


def write_to_css(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"],
        subject = data["subject"],
        message = data["message"],
        date = time()
        csv_writer = csv.writer(database, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message, date])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit the form from contact and add the information to the mongDB Database"""
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            add_new_contact(data)
        except:
            write_to_css(data)
        return redirect('thankyou.html')
    else:
        return "Something went wrong. Try again!"


if __name__ == '__main__':
    app.run()
