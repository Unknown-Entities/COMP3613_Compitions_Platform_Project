from App.models import User
from App.models import Student, admin 
from App.database import db

def create_user(username, password, email):
    newuser = User(username=username, password=password, email=email)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
"""
Above code probably required, more testing is required;below is what I think
is the correct implementation following the above format. Granted this is being
written without the model code written.
"""

def create_student(username, password): #creates student object
    newUser = Student(username=username, password=password)

    try:
        db.session.add(newUser)
        db.session.commit()
        return newUser
    
    except:
        return None

def create_admin(username, password): #creates student object
    newUser = Admin(username=username, password=password)

    try:
        db.session.add(newUser)
        db.session.commit()
        return newUser
    
    except:
        return None

def fetchProfile(profileId):
    profile = User.query.get(profileId)

    if profile:
        return profile.toJSON()

    return f'{profileId} profile not found'

def get_admin(id):
    return Admin.query.get(id)

def get_student(id):
    return Student.query.get(id)

def update_admin(id, username):
    user = get_admin(id)

    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def update_student(id, username):
    user = get_student(id)

    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

#TODO: write helper function

