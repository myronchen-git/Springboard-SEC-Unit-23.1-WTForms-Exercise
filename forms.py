from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField
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
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(message="Invalid URL."),
            Optional()
        ]
    )
    age = IntegerField(
        "Age",
        validators=[
            NumberRange(min=0, max=30, message="Age must be between 0 and 30."),
            Optional()
        ]
    )
    notes = StringField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(message="Invalid URL."),
            Optional()
        ]
    )
    notes = StringField(
        "Notes",
        validators=[Optional()]
    )
    available = BooleanField("Available")
