from enum import unique
import os
from flask import Flask, render_template, redirect, url_for, session, request, flash, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  
from forms import TransectionForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'development key'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bank'


#table users for storing users
class Users(db.Model):
    __tablename__ = 'users'
    sr_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    balance = db.Column(db.Float(), unique=False, nullable=False)

#table transections for users
class Transections(db.Model):
    __tablename__ = 'transections'
    sr_no = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(20), unique=False, nullable=False)
    to_user = db.Column(db.String(20), unique=False, nullable=False)
    amount_transfered = db.Column(db.Float(), unique=False, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow())

    @classmethod
    def trans(cls,from_user,to_user,amount_transfered):
        trans=cls(from_user=from_user,
                  to_user=to_user,
                  amount_transfered=amount_transfered
                 )
        db.session.add(trans)
        db.session.commit()

    def is_active(self):
        # all users are active
        return True

    def get_id(self):
        return (self.Id)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        # False as we do not support annonymity
        return False


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/user/', methods = ['GET', 'POST'])
def user():
    users=Users.query.all()
    return render_template('user.html', users=users)



@app.route('/transection_history', methods = ['GET', 'POST'])
def transection_history():
    transe=Transections.query.all()
    return render_template('transection_history.html', employeeleave=transe)



@app.route('/transections', methods = ['GET', 'POST'])
def transections():
    form=TransectionForm()
    if form.validate_on_submit():
        Transections.trans(
            from_user=form.from_user.data,
            to_user=form.to_user.data,
            amount_transfered=form.amount_transfered.data
            )
        flash('Transection Successful!!', category='success')
        return redirect(url_for('transection_history'))
    return render_template('transections.html',form=form)
    

    
@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')



if __name__ == '__main__':
    db.create_all()

app.run(debug=True)