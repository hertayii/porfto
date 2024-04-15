import json
import os.path
import csv

from flask import Flask, render_template, url_for, send_from_directory, request, redirect

app = Flask(__name__)


# path = 'templates'
# for filename in os.listdir(path):
#     print(filename)

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('db.csv', newline='', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'form not submitted'
#
#
# @app.route("/works.html")
# def works_page():
#     return render_template("works.html")
#
#
# @app.route("/about.html")
# def about_page():
#     return render_template("about.html")
#
#
# @app.route("/contact.html")
# def contact_page():
#     return render_template("contact.html")
#
# @app.route("/components.html")
# def components_page():
#     return render_template("components.html")
