from datetime import datetime
import csv


def write_to_css(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"],
        subject = data["subject"],
        message = data["message"],
        date = datetime.now()
        csv_writer = csv.writer(database, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message, date])
