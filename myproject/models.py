
from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
class User(db.Model,UserMixin):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key='True')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
class pay(db.Model):
    __tablename__='payments'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(45))
    Owner=db.Column(db.String(64))
    Cvv=db.Column(db.String(70),unique=True)
    Card=db.Column(db.String(50),unique=True)
    Month=db.Column(db.String(30))
    year=db.Column(db.String(20))
    amount=db.Column(db.String(10))

    def __init__(self,name,Owner,Cvv,Card,Month,year,amount):
     self.name=name
     self.Owner=Owner
     self.Cvv=Cvv
     self.Card=Card
     self.Month=Month
     self.year=year
     self.amount=amount

class donations(db.Model):
    __tablename__='donations'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    address=db.Column(db.String(100))
    mobile=db.Column(db.String(100))
    item1=db.Column(db.String(100))
    item2=db.Column(db.String(100))
    item3=db.Column(db.String(100))
    item4=db.Column(db.String(100))
    item5=db.Column(db.String(100))
    item6=db.Column(db.String(100))


    def __init__(self,name,address,mobile,item1,item2,item3,item4,item5,item6):
       self.name=name
       self.address=address
       self.mobile=mobile
       self.item1=item1
       self.item2=item2
       self.item3=item3
       self.item4=item4
       self.item5=item5
       self.item6=item6