import csv

from flask import Flask
from flask import request

application = Flask(__name__)

@application.route("/")
def hello():

    return "Hello World!"

if __name__ == "__main__":

    application.run()

@application.route('/casestudy')
def casestudy():
    region = request.args.get('region')
    product = request.args.get('product')
    with open('casestudy.csv', 'r') as csvfile:
        customers = csv.reader(csvfile, delimiter=',', quotechar='|')
        customermatches=""
        for row in customers:       
            if row[1].find(region) != -1 and row[3].find(product) != -1:
                customermatches = customermatches+ "<p><a href='"+row[4]+"'>"+row[0]+"</a>"
    return "<h1>Matching customers</h1>\n<h3>"+customermatches+"</h3>"
