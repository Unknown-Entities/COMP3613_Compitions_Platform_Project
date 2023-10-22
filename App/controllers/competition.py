from App.models import competition, admin, student
from App.database import db

def create_comp(competitionName, prize, region, maxEntrants: int):
    newcomp = Competition(competitionName, prize, region, maxEntrants)
    db.session.add(newcomp)
    db.session.commit()
    return newcomp

def add_result(compId, winnerId):
    competition = Competition.query.get(compId)
    winner = Student.query.get(winnerId)

    if competition and winner:
        return admin.addResult(competition.id, winner.id)
        #should add winner.id to the specificied competition
    return False #unable to add winner

def view_competitions():
    return Competition.query.all() #can be then manipulated and displayed

def get_comp(id)
    return Competition.query.get(id)

#TODO: add helper functions
