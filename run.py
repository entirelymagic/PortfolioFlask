from flask import Flask, render_template, request, redirect, send_from_directory
from data.db import add_new_contact
from data.csv_db.write_to_csv import write_to_css

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def my_home():
    """render home and index template"""
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    """Render and return the html template provided as page_name"""
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Submit the form from contact and add the information to the mongoDB Database.
    If connection is close, write to local css file.
    """

    if request.method in ['POST', 'GET']:
        data = request.form.to_dict()
        try:
            add_new_contact(data)
        except:
            write_to_css(data)
        return redirect('thankyou.html')
    else:
        return "Something went wrong. Try again!"


@app.route("/robots.txt")
def robots_txt():
    return render_template("robots.txt")


if __name__ == '__main__':
    app.run()
