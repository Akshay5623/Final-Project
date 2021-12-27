from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TeamForm(FlaskForm):
    teamname = StringField("Team Name", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    submit = SubmitField("Submit Team Name and City")

class PlayersForm(FlaskForm):
    pointguard = StringField("Select your Point Guard", validators=[DataRequired()])
    shootingguard = StringField("Select your Shooting Guard", validators=[DataRequired()])
    smallforward = StringField("Select your Small Forward", validators=[DataRequired()])
    powerforward = StringField("Select your Power Forward", validators=[DataRequired()])
    center = StringField("Select your Center", validators=[DataRequired()])
    submit = SubmitField("Confirm your Players")
#