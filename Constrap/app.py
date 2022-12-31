import mysql.connector as mys
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from random import *
import smtplib

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'constrapTS@gmail.com'
app.config["MAIL_PASSWORD"] = 'vmlzdeaayffrguhe'
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


computer_genereted_otp = ""


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        mycon = mys.connect(host='localhost', user='root',
                            passwd='password', database="constrap")
        mycursor = mycon.cursor()
        mycursor.execute("select * from logindetails")
        for i in mycursor:
            if email == i[0] and password == i[1]:
                return render_template('none.html')
            else:
                return render_template('index.html')


@app.route('/otp', methods=['POST'])
def otp():
    if request.method == 'POST':
        user_entered_otp = request.form['otp']
        if computer_genereted_otp == user_entered_otp:
            return render_template('none.html')
        else:
            return render_template('otp.html')


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except:
        pass


"""        msg = Message(
            subject='OTP', sender="constapTS@gmail.com", recipients=["21204003@rmd.ac.in"])
        global computer_genereted_otp
        computer_genereted_otp = str(randint(1000, 9999))
        msg.body = "Your OTP is " + computer_genereted_otp
        mail.send(msg)

    return render_template('otp.html')

"""
