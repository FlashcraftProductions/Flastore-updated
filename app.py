from flask import Flask, render_template, request, url_for, flash, redirect
from flask_mail import Mail, Message


# flashcraftproductions@gmail.com
# Mystartup@2023

app = Flask(__name__)

app.secret_key = "mail"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']= 'flashcraftproductions@gmail.com'
app.config['MAIL_PASSWORD']='hvsgqqckrppolisc'

mail= Mail(app)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method =='POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        contact = request.form['contact']
        message = request.form['message']
        
        msg = Message('New Form Submission',
                      sender= 'flashcraftproductions@gmail.com',
                      recipients=['flashcraftproductions@gmail.com'])
        msg.body=f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nContact No: {contact}\nMessage: {message}"
                    
        mail.send(msg)
        flash('Your enquiry hasbeen submitted, our team will be getting back to you soon...')
        return redirect(url_for('home'))
        
    return render_template('index.html')

@app.route('/bussiness_card')
def bussiness_card():
    return render_template('businesscard.html')



@app.route('/apparel')
def apparel():
    return render_template('comingsoon.html')

@app.route('/socialmedia')
def socialmedia():
    return render_template('socialmedia.html')

@app.route('/standee')
def standee():
    return render_template('standee.html')

@app.route('/brochure')
def brochure():
    return render_template('brochure.html')

@app.route('/invitation')
def invitation():
    return render_template('invitation.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/webdesign')
def webdesign():
    return render_template('webdesign.html')

@app.route('/stainory')
def stainory():
    return render_template('stainory.html')

@app.route('/Coming')
def Coming():
    return render_template('Comingsoon.html')


if __name__ == '__main__':
    app.run(debug=True)
