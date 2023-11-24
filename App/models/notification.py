from App.database import db
from datetime import datetime 

class Notification(db.Model):
    notificationID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer,  db.ForeignKey('student.id'))
    student_email = db.Column(db.String, db.ForeignKey('user.email'))
    message = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())

def __init__(self, studentID, message, student_email):
    self.studentID = studentID
    self.message = message
    self.student_email = student_email

    def toJSON(self):
        return {
            'notificationID' : self.notificationID,
            'studentID' : self.studentID,
            'message' : self.message,
            'student_email': self.student_email,
            'timestamp': self.payment_date.strftime("%Y/%m/%d, %H:%M:%S")
        }
    
