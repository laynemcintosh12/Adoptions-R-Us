from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL
from species import species


class AddPetForm(FlaskForm):
    """Form to add a new pet"""

    name = StringField("Pet Name", 
                       validators=[InputRequired(message="Name Can Not Be Blank")])
    species = SelectField("Species", 
                          choices=[(sp,sp) for sp in species],
                          validators=[InputRequired(message="Species Can Not Be Blank")])
    pic = StringField("Picture URL", 
                      validators=[Optional(), URL(require_tld=False, 
                                                  message='Please Enter A Valid URL')])
    age = IntegerField("Age", 
                       validators=[Optional(), NumberRange(min='1', max='30',
                                                           message='Please Enter A Valid Age')])
    notes = StringField("Notes", 
                        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    pic = StringField("Photo URL",
                            validators=[Optional(), URL()],)
    notes = TextAreaField("Comments",
                          validators=[Optional()])
    avb = BooleanField("Available?")