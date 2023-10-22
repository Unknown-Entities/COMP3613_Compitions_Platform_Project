import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Admin, Auth
from App.controllers import * #TDOD: change to only import reqiuired functions


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_create_user(self):
        testUser = Admin("maraval", "maravalpass")
        assert testUser.username == "maraval"

    #maybe change to test admin/student.toJSON()
    def test_get_json(self):
        user = Admin("maraval", "maravalpass")
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id": None, "username":"maraval", "user_type":"admin"})
    
    def test_hashed_password(self):
        password = "testpass"
        hashed = generate_password_hash(password, method='sha256') #maybe not needed? I think it should auto hash;will leave it for now
        user = User("maraval", hashed)
        assert user.password != hashed

    def test_check_password(self):
        password = "testpass"
        user = User("maraval", password)
        assert user.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_jwt_authenticate():
    user = create_admin("maraval", "maravalpass")
    token = jwt_authenticate("maraval", "maravalpass")
    self.assertIsNotNone(token, "")

def test_create_admin():
    sando = create_admin("sando", "sandopass")
    user = get_admin(sando.id)
    assert user.username == sando.username

class UsersIntegrationTests(unittest.TestCase):

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"maraval"}, {"id":2, "username":"sando"}], users_json)

    def test_update_admin(self):
        update_admin(1, "freeport")
        user = get_admin(1)
        assert user.username == "freeport"

    def test_admin_add_comp(self):
        user = create_admin("maraval", "maravalpass")
        comp = user.add_comp("walktime", "2 dabloons", "NA", 21)
        self.assertIsNotNone(comp, "")

    def test_admin_add_result(self)

    #TODO: test_admin_add_comp(), test_admin_add_result()
