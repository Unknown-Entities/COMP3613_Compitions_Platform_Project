from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import(
  createComp,
  addResult,
  viewCompetitons,
)

competition_views = Blueprint('competition_views', __name__, template_folder='../templates')

@competition_views.route('/competitions', methods=['GET'])
def viewCompetitions_action():
  competitions = viewCompetitions()
  return jsonify(competitons)

@competition_views.route('/competitions', methods=['POST'])
@jwt_required()
def createComp_action():
  competition = createComp()
  return competition

@competitions_views.route('/competitions', methods=['POST'])
@jwt_required()
def addResult_action():
  result = addResult(data['compId'], data['winnerId']  
  if result:
    return result
  return False
 



  
