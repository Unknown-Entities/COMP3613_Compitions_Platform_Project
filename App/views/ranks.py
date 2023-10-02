from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import(
  fetchRanks,
  filterRanks
)

ranks_views = Blueprint('ranks_views', __name__, template_folder='../templates')

@ranks_views.route('/ranks', methods=['GET'])
def fetchRanks_action():
  fetchRanks()

@ranks_views.route('/ranks', methods=['GET'])
def filterRanks_action():
  filterRanks()
