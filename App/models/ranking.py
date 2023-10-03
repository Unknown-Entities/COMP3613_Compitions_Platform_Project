from App.database import db
from .notification import Notification

class Ranking(db.Model):
    rankingID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'))
    competitionID = db.Column(db.Integer, db.ForeignKey('competition.id'))
    name = db.Column(db.String(120), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(300), nullable=False)

    def __init__(self, studentID, competitionID, name, rank, university):
        self.studentID = studentID
        self.competitionID = competitionID
        self.name = name
        self.rank = rank
        self.university = university

    def __repr__(self):
        return f'<ranking {self.rankingID} name: {self.name} rank: {self.rank} university: {self.university}>'
    
    def toJSON(self):
        return{
            'rankingID': self.rankingID,
            'studentID': self.studentID,
            'competitionID': self.competitionID,
            'name': self.name,
            'rank': self.rank,
            'university': self.university
        }

    #TODO: notify student function