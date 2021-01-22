import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://flask_db_user:flask_db_pass@portfolio.bqtz2.mongodb.net/portfolio?retryWrites=true&w=majority"
)
db = client.portfolio  # set the database to portfolio


def add_new_contact(data):
    """Insert into the portfolio database, contact_details (data is a dictionary)"""
    db.contact_details.insert({
        'email': data['email'],
        'subject': data['subject'],
        'message': data['message']
    })
