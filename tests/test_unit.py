from flask_testing import TestCase
from application import app, db
from application.models import Teams, Players
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        team = Teams(city="London", teamname="Lions")
        player = Players(pointguard="Joe_Bloggs", shootingguard="John_Smith", smallforward="Dave_Jones", powerforward="Steve_Jenkins", center="Keith_Palmer", team_id="1") # needed to add team_id to fix one of the failed tests
        db.session.add(team)
        db.session.add(player)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_create_team_get(self):
        response = self.client.get(url_for('create_team', team_id=1))
        self.assertEqual(response.status_code, 200)  

    def test_update_team_get(self):
        response = self.client.get(url_for('update_team', team_id=1))
        self.assertEqual(response.status_code, 200)  

    def test_create_players_get(self):
        response = self.client.get(url_for('create_players', team_id=1))      
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):

    def test_read_teams(self):
        response = self.client.get(url_for("home"))
        self.assertIn('London', str(response.data))
        # another way of writing it is --> self.assertIn(b'London', response.data)

    def test_read_players(self):
        response = self.client.get(url_for("home"))
        self.assertIn('Joe_Bloggs', str(response.data))

class TestCreate(TestBase):

    def test_create_team(self):
        response = self.client.post(
            url_for("create_team"),
            json={"city":"Peterborough", "teamname":"Panthers"},
            follow_redirects=True
        )
        new_team = Teams.query.get(2)
        self.assertEqual("Peterborough", new_team.city)
        self.assertEqual("Panthers", new_team.teamname)

    def test_create_team_redirect(self):
        response = self.client.post(
            url_for("create_team"),
            json={"city":"Vegas", "teamname":"Victory"},
            follow_redirects=True
        )
        self.assertIn('Vegas', str(response.data))
        self.assertIn('Victory', str(response.data))

    def test_create_players(self):
        response = self.client.post(
            url_for('create_players', team_id=1),
            json={'pointguard':'Steve_Jones', 'shootingguard':'David_Wong', 'smallforward':'Matt_Collins', 'powerforward':'Ryan_Rose', 'center':'Sean_Richardson', 'team_id':'1'},
            follow_redirects=True
        )
        new_players = Players.query.get(2)
        self.assertEqual('Steve_Jones', new_players.pointguard)
        self.assertEqual('David_Wong', new_players.shootingguard)
        self.assertEqual('Matt_Collins', new_players.smallforward)
        self.assertEqual('Ryan_Rose', new_players.powerforward)
        self.assertEqual('Sean_Richardson', new_players.center)

class TestUpdate(TestBase):

    def test_update_team(self):
        response = self.client.post(
            url_for("update_team", team_id=1),
            json={"city":"Seattle", "teamname":"Scorpions"},
            follow_redirects=True
        )
        new_team = Teams.query.get(1)
        self.assertEqual("Seattle", new_team.city)
        self.assertEqual("Scorpions", new_team.teamname)

    def test_update_players(self):
        response = self.client.post(
            url_for('update_players', player_id=1),
            json={'pointguard':'Stephen_Lawson', 'shootingguard':'Devin_Davis', 'smallforward':'Leon_James', 'powerforward':'Anthony_James', 'center':'Rudy_Jenkins', 'team_id':'1'},
            follow_redirects=True
        )
        new_players = Players.query.get(1)
        self.assertEqual('Stephen_Lawson', new_players.pointguard)
        self.assertEqual('Devin_Davis', new_players.shootingguard)
        self.assertEqual('Leon_James', new_players.smallforward)
        self.assertEqual('Anthony_James', new_players.powerforward)
        self.assertEqual('Rudy_Jenkins', new_players.center)
   
class TestDelete(TestBase):

    def test_delete_team(self):
        response = self.client.get(url_for('delete_team', team_id=1))
        new_team = Teams.query.filter_by(team_id=1).scalar() # fixed test failure by adding .scalar() --> .scalar can be used with queries
        self.assertEqual(None, new_team)  
        
    def test_delete_players(self):
        response = self.client.get(url_for('delete_players', player_id=1))
        new_players = Players.query.filter_by(player_id=1).scalar() # fixed test failure by adding .scalar() --> .scalar can be used with queries
        self.assertEqual(None, new_players)

