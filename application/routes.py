from application import app, db
from application.models import Teams, Players
from application.forms import TeamForm, PlayersForm
from flask import render_template, request, url_for, redirect, jsonify, Response

@app.route('/')
def home():
    all_teams = Teams.query.all()
    return render_template("index.html", title="Home", all_teams=all_teams)

@app.route('/create-team', methods=["GET","POST"])
def create_team():
    form = TeamForm()
    form.submit.label.text= "Add Team Name and City"
    
    if request.method == "POST":
        new_team = Teams(teamname=form.teamname.data, city=form.city.data)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for("home")) 

    return render_template("team_form.html", title="Create Your Team Name", form=form)

@app.route('/create-players/<int:team_id>', methods=['GET','POST'])
def create_players(team_id):
    form = PlayersForm()
    form.submit.label.text = "Add Players"

    if request.method=='POST':
        new_players = Players(pointguard=form.pointguard.data, shootingguard=form.shootingguard.data, smallforward=form.smallforward.data, powerforward=form.powerforward.data, center=form.center.data, team_id=team_id)
        db.session.add(new_players)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("players_form.html", title="Add your Players", form=form)

