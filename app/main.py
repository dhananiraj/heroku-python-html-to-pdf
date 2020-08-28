from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return "This is the api made by Raj Dhanani and Shubham Bhanderi from RS Tech"


