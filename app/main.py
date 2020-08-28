from flask import *
from flask_cors import CORS
from pdfkit import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def home_view():
    from_string("This is the api made by Raj Dhanani and Shubham Bhanderi from RS Tech", 'temp.pdf')
    return send_file("temp.pdf")


