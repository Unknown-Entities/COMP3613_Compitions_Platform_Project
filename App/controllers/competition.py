#from App.models import Competition, Admin, Student
from App.database import db

def createComp(competitionName, prize, region, maxEntrants: int):
    return admin.createComp(competitionName=competitionName, prize=prize, region=region, maxEntrants=maxEntrants)
    #should create a new competition object from the provided info then add it to the db and return it

def addResult(compId, winnerId):
    competition = Competition.query.get(compId)
    winner = Student.query.get(winnerId)

    if competition and winner:
        return admin.addResult(competition.id, winner.id)
        #should winner.id to the specificied competition
    return False #unable to add winner

def viewCompetitions():
    return Competition.query.all() #can be then manipulated and displayed

#TODO: add helper functions