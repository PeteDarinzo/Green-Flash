from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, IntegerField, TextField, TextAreaField
from wtforms.validators import InputRequired, ValidationError


#DATE PICKER FORM:
# https://www.youtube.com/watch?v=jAdFZa6KZNE


class BusinessSearchForm(FlaskForm):
    """Form for business search submit."""

    category = StringField("Category", validators=[InputRequired(message="This field is required.")])

    city = StringField("Location", validators=[InputRequired(message="This field is required.")])


class LogForm(FlaskForm):
    """Form to submit a new log."""

    title = StringField("Title", render_kw={'class': 'form-control', 'placeholder' : 'Title'}, validators=[InputRequired(message="This field is required.")])

    location = StringField("Location", render_kw={'class': 'form-control', 'placeholder' : 'City, State'})

    mileage = IntegerField("Mileage", render_kw={'class': 'form-control', 'placeholder' : 'Mileage'})

    text = TextAreaField("Body", render_kw={'class': 'form-control'}, validators=[InputRequired("This field is required.")])


class MaintenanceForm(FlaskForm):
    """Form to submit a new maintenance event."""

    date = StringField("Date", render_kw={'class': 'form-control', 'placeholder' : 'Date'}, validators=[InputRequired(message="This field is required.")])

    mileage = IntegerField("Mileage", render_kw={'class': 'form-control', 'placeholder' : 'Mileage'})

    location = StringField("Location", render_kw={'class': 'form-control', 'placeholder' : 'City, State'}, validators=[InputRequired("This field is required.")])

    title = StringField("Title", render_kw={'class': 'form-control', 'placeholder' : 'Title'}, validators=[InputRequired(message="This field is required.")])

    description = TextAreaField("Body", render_kw={'class': 'form-control'}, validators=[InputRequired("This field is required.")])
