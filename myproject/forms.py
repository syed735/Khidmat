from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

from myproject.models import User

class LoginForm(FlaskForm):
    email= StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')







class RegistrationForm(FlaskForm):
    email= StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email is already registered!')

    def check_username(self, field):
            # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
  
class donate_item(FlaskForm):
    address=StringField('address',validators=[DataRequired()])
    mobile=IntegerField("Mobile",validators=[DataRequired()])
    item1=SelectField('Item1',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    item2=SelectField('Item1',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    item3=SelectField('Item1',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    item4=SelectField('Item4',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    item5=SelectField('Item5',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    item6=SelectField('Item6',choices=[('none','None'),('furniture','Furniture'),('dinnerware','Dinnerware'),('clothes','Clothes'),('electrical appliances','Electrical Appliances'),('footwear','Footwear'),('winterwear','Winterwear'),('books','Books'),('stationery','Stationery'),('plastic items','Plastic Items')])
    submit=SubmitField('Donate')


class pay_me(FlaskForm):
     Owner=StringField('owner',validators=[DataRequired()])
     Cvv=IntegerField('cvv',validators=[DataRequired()])
     Card=IntegerField('cardno',validators=[DataRequired()])
     Month=SelectField('Months',choices=[('jan','Jan'),('feb','Feb'),('march','Mar'),('apr','Apr'),('may','May'),('jun','Jun'),('jul','Jul'),('aug','Aug'),('sept','Sept'),('oct','Oct'),('nov','Nov'),('dec','Dec')])
     year=SelectField('Year',choices=[('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025')])
     amount=IntegerField('AMOUNT',validators=[DataRequired()])
     submit=SubmitField('Confirm')