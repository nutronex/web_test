from flask import Flask,render_template,flash,redirect,url_for

from app.forms import LoginForm,RegistrationForm
from app.config import Config
from app.models import User
from app import db

from flask_login import current_user,login_user,logout_user,login_required

#app = Flask(__name__)
from app import flask_app

@flask_app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))




@flask_app.route("/protected")
@login_required
def protected():
    return "this is protected view"

@flask_app.route("/")
@flask_app.route("/index")
def index():
    posts = [{'author_name':"myo ko",'body':"hello world"},{'author_name':'ko lat','body':"fuck you"}]
    return render_template("index.html",title="my title", name=" fooooo",posts= posts , form = LoginForm())



@flask_app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.name.data,email=form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html",form=form)

@flask_app.route('/login',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        print("authenticated user")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid user login")
            return redirect(url_for("login"))
        print("login successful")
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for("index"))

    return render_template("login.html", form = form)

@flask_app.route("/user/<username>")
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [{"author":"test","post":"test post"},{"author":"test2","post":"test post2"}]
    return render_template("user.html",user=user,posts=posts)




if __name__ == "__main__":
    app.run()



