from flask import *
from flask_cors import CORS
from pdfkit import *
import random

app = Flask(__name__)
CORS(app)

# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
path_wkhtmltopdf = r'/app/bin/wkhtmltopdf'

config = configuration(wkhtmltopdf=path_wkhtmltopdf,options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.3in',
    'margin-bottom': '0.75in',
    'margin-left': '0.3in',
    'encoding': "UTF-8",
    'custom-header' : [('Accept-Encoding', 'gzip')],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}
)

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
    fn = random.randint(1000, 10000)
    from_string(string['data'].replace(',','').replace('undefined',''),f"./app/pdfs/{fn}.pdf" ,configuration=config)
    return send_file(f"./pdfs/{fn}.pdf")


@app.route("/from-url", methods=["POST"])
def render_view_from_url():
    string = request.get_json()
    fn = random.randint(1000, 10000)
    from_url(string['url'],f"./app/pdfs/{fn}.pdf" ,configuration=config)
    return send_file(f"./pdfs/{fn}.pdf")