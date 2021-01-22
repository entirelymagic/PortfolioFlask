import csv

from flask import Flask, render_template, request, redirect
from data.db import add_new_contact


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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit the form from contact and add the information to the mongDB Database"""
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            add_new_contact(data)
            return redirect('thankyou.html')
        except:
            return ' Did not save to DB'
    else:
        return "Something went wrong. Try again!"


if __name__ == '__main__':
    app.run()
