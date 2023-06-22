from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

from contact_form import ContactForm

app = Flask(__name__)
app.config.from_object('config')

mail = Mail()
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