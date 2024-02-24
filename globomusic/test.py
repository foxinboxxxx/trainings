import os
import unittest
from config import basedir
from app import app, db
from app.models import User

class TestExample(unittest.TestCase):
    def setUp(self):
        # Happens before each test
        self.app_test_client = app.test_client()
        db.create_all()

    def tearDown(self):
        # Happens after each test
        db.session.remove()
        db.drop_all()

    def test_home_route(self):
        resp = self.app_test_client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_user_creation(self):
        u = User(username="test", email="test@mail.com")
        u.set_password("password123")
        db.session.add(u)
        db.session.commit()
        u = User.query.filter_by(username="test").first()
        assert u.username == "test"
        assert u.check_password("password123")

if __name__ == "__main__":
    unittest.main()
