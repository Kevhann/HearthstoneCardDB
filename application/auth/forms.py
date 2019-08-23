from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from application.auth.models import User
from wtforms.validators import ValidationError

class Unique(object):
    """ validator that checks field uniqueness """
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'this element already exists'
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class LoginForm(FlaskForm):
  username = StringField("Username")
  password = PasswordField("Password")
  
  class Meta:
    csrf = False

class CreateUserForm(FlaskForm):
  name = StringField("Name", [validators.Length(min=2)])
  username = StringField("Username", [validators.Length(min=2), Unique(User, User.username)]) 
  password = PasswordField("Password", [validators.Length(min=2)])

  class Meta:
    csrf = False

