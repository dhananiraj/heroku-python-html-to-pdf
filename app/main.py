from flask import *
from flask_cors import CORS
from pdfkit import *
import random

app = Flask(__name__)
CORS(app)

# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
path_wkhtmltopdf = r'/usr/local/bin/wkhtmltopdf'

config = configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.route("/", methods=["GET"])
def home_view():
    # from_string("This is the api made by Raj Dhanani and Shubham Bhanderi from RS Tech", 'temp.pdf', configuration=config)
    from_string("""Hello world this is the HTML to PDF Api Made by Raj and Shubham from RS Tech\n
        To convert your HTML make a POST Request to temp-testing-app.herokuapp.com\n
        Have fun ... BIEATCHESSS (Jessi Pinkman) ... pass object as { data : "HTML STRING" }
    ""","./app/pdfs/temp.pdf" ,configuration=config)
    return send_file("./pdfs/temp.pdf")

@app.route("/", methods=["POST"])
def render_view():
    string = request.get_json()
    # print(request, string)
    # return "s"
    fn = random.randint(1000, 10000)
    from_string(string['data'],f"./app/pdfs/{fn}.pdf" ,configuration=config)
    return send_file(f"./pdfs/{fn}.pdf")

