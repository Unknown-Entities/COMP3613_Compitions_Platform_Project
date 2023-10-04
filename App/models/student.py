from .user import User
from App.database import db 

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    profile = db.relationship('Profile', backref=db.backref('student', lazy='joined'))
    competition = db.relationship('Competition', backref=db.backref('competitor', lazy='joined'))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = "student"

    def __repr__(self):
        return f'<Student {self.id} {self.username}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': 'student'
        }