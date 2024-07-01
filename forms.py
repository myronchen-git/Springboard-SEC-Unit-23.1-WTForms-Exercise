from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField

# ==================================================

class AddPetForm(FlaskForm):
    """Form to add a pet."""

    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
