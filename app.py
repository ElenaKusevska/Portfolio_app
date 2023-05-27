from flask import Flask, render_template, request
from flask_mail import Mail, Message

from dotenv import load_dotenv   
load_dotenv()                   

import os 


app = Flask(__name__)

mail = Mail()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)


@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/contactme", methods=['GET', 'POST'])
def contactme():
    if request.method == 'POST':
        msg = Message("hey", sender='elena.kusevska.contactform@gmail.com', recipients=['elena.kusevska@gmail.com'])

        msg.body = "Hey Elena!"
        mail.send(msg)
        return render_template("contactme.html", message="sent")

    return render_template("contactme.html")

if __name__ == '__main__':
    app.run(debug=True)