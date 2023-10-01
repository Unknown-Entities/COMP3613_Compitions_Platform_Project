from App.database import db 

class Competition(db.Model):
    competitionID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    compName = db.Column(db.String(120), nullable=False)
    prize = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(120), nullable=False)
    maxEntrants = db.Column(db.Integer, nullable=False)
    rankings = db.relationship('Ranking', backref=db.backref('competition', lazy='joined'))

def __repr__(self):
    return f'<Competition {self.competitionID} - {self.compName}>'

def toJSON(self):
    return {
        'competitionID': self.competitionID,
        'studentID': self.studentID,
        'compName': self.compName,
        'prize': self.prize,
        'region': self.region,
        'maxEntrants': self.maxEntrants
    }