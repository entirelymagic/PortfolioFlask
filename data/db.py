import pymongo
from time import time


def add_new_contact(data):
    """Connect to DB and add data from the form."""
    client = pymongo.MongoClient(
        "mongodb+srv://flask_db_user:flask_db_pass@portfolio.bqtz2.mongodb.net/portfolio?retryWrites=true&w=majority",
        connectTimeoutMS=3000,
        socketTimeoutMS=None,
        socketKeepAlive=True,
        connect=False,
        maxPoolsize=1
    )
    db = client.portfolio  # set the database to portfolio

    db.contact_details.insert({
        'email': data['email'],
        'subject': data['subject'],
        'message': data['message'],
        'date': time()
    })