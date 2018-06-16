from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo,Email,ValidationError
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField
from app.models import User

class LoginForm(FlaskForm):
    name = StringField("Uname", validators = [DataRequired()])
    password = PasswordField("Passwd", validators = [DataRequired()])
    remember_me = BooleanField("Remember")
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    name = StringField("user name",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired(),Email()])
    password1 = StringField("password",validators=[DataRequired()])
    password2 = StringField("confirm password",validators=[DataRequired(),EqualTo("password1")])
    submit = SubmitField("register")

    def validate_name(self,name):
        u = User.query.filter_by(username=self.name.data).first()
        if not u is None:
            raise ValidationError("use different username")

    def validate_email(self,email):
        u = User.query.filter_by(email=self.email.data).first()
        if not u is None:
            raise ValidationError("use different email address")





