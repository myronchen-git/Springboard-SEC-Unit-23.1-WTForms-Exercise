from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField
from wtforms.validators import URL, AnyOf, InputRequired, NumberRange, Optional

# ==================================================

class AddPetForm(FlaskForm):
    """Form to add a pet."""

    name = StringField(
        "Name",
        validators=[
            InputRequired(message="Name is required.")
        ]
    )
    species = StringField(
        "Species",
        validators=[
            AnyOf(values=["cat", "dog", "porcupine"], message="Invalid species."),
            InputRequired(message="Species is required.")
        ]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(message="Invalid URL.")
        ]
    )
    age = IntegerField(
        "Age",
        validators=[
            NumberRange(min=0, max=30, message="Age must be between 0 and 30.")
        ]
    )
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form to edit a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(message="Invalid URL.")
        ]
    )
    notes = StringField(
        "Notes",
        validators=[Optional()]
    )
    available = BooleanField("Available")
