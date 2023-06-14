from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from contact_form import ContactForm

from dotenv import load_dotenv   
load_dotenv()                   

import os 


app = Flask(__name__)

mail = Mail()

app.config['SECRET_KEY'] = 'ABCDEFGH'
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
    form = ContactForm()

    if request.method == 'POST':
        if form.validate():
            name = request.form.get('name')
            email = request.form.get('email')
            msg = Message("You've got mail!", 
                           sender='elena.kusevska.contactform@gmail.com', 
                           recipients=['elena.kusevska@gmail.com']
                         )

            msg.body = " New message from: " + name + " " + email

            mail.send(msg)
            return jsonify({"status": "Message Sent"})
        else:
            return jsonify({"status": form.errors})
    else:
        return render_template("contactme.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)