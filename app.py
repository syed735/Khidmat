import os

from flask import Flask
from myproject import  app,db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user,login_required,logout_user,current_user
from myproject.models import User,pay,donations
from myproject.forms import LoginForm,RegistrationForm,donate_item,pay_me
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

@app.route('/adminblog')
def admin():
     email= request.args.get('email')
     password=request.args.get('password')
     if email =="sufiyan@admin.com" and password=="syed@123":
        return redirect('/admin')
     return render_template('adminlogin.html',email=email,password=password)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')
    


@app.route('/thankyou')
def thankyou():
    Firstname=request.args.get('Firstname')
    Lastname=request.args.get('Lastname')
    return render_template('thankyou.html',Firstname=Firstname,Lastname=Lastname)





@app.route('/thankyou2')
def thankyou2():
     username=request.args.get('username')
     password=request.args.get('password')
     email=request.args.get('email')
     return render_template('thankyou2.html',username=username,password=password,email=email)
     


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')
        else:  
            return redirect(url_for('thankyou3'))




            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
        next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
        if next == None or not next[0]=='/':
            next = url_for('index')

        return redirect(next)
    return render_template('loginform.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('thankyou2'))
    return render_template('register.html', form=form)
 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged Out')
    return redirect(url_for('home'))
    
admin=Admin(app)
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(pay,db.session))
admin.add_view(ModelView(donations,db.session))

@app.route('/thankyou3')
def thankyou3():
      return render_template('thankyou3.html')



@app.route('/payment',methods=['GET','POST'])

def payment():
    form=pay_me()
    if form.validate_on_submit():
        p=pay(name=current_user.username, Owner=form.Owner.data,Cvv=form.Cvv.data,Card=form.Card.data,Month=form.Month.data,year=form.year.data,amount=form.amount.data)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('thankyou'))
    
    return render_template('payment.html',form=form)
    


@app.route('/charity',methods=['GET','POST'])
def charity():
    form=donate_item()
    if form.validate_on_submit():
        char=donations(name=current_user.username,address=form.address.data,mobile=form.mobile.data,item1=form.item1.data,item2=form.item2.data,item3=form.item3.data,item4=form.item4.data,item5=form.item5.data,item6=form.item6.data)
        db.session.add(char)
        db.session.commit()
        return redirect(url_for('thankyou'))

    return render_template('donate_page.html',form=form)



if __name__ == '__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
