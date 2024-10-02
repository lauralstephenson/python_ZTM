#import csv module so we can save form data
import csv

from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")


#this renders each page in the folder templates
@app.route("/<string:page_name>")
def html_page(page_name):
  return render_template(page_name)


def write_to_file(data):
  with open("database.text", mode="a") as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2,
                            delimiter=",",
                            quotechar="'",
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
  if request.method == "POST":
    data = request.form.to_dict()
    write_to_csv(data)
    return redirect("/thankyou.html")
  else:
    return "Something went wrong. Try again!"


if __name__ == '__main__':
  app.run(host='0.0.0.0')

