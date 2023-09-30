#from App.models import Ranks
from App.database import db

def fetchRanks():
    return Ranks.query.all() #can be then manipulated and displayed

def filterRanks(university, topx: int ):
    return Ranks.query.filter_by(university).all() #TODO: find a way to return only the to 20 if not can always just use this and display where id in range 1 to 20