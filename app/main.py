from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home_view():
    return "This is the api made by Raj Dhanani and Shubham Bhanderi from RS Tech"


