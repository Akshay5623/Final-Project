from application import db

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    players = db.relationship('Players', cascade="all", backref='team') # Cascade all allows for deletion of players by deleting the team too.

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    pointguard = db.Column(db.String(255), nullable=False)
    shootingguard = db.Column(db.String(255), nullable=False)
    smallforward = db.Column(db.String(255), nullable=False)
    powerforward = db.Column(db.String(255), nullable=False)
    center = db.Column(db.String(255), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)

# class Players(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     player_name = db.Column(db.String(255))
#     position = db.Column(db.String(255))
#     players_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

