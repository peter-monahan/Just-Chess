from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def users():
    users = User.query.all()
    return {user.id: user.to_dict() for user in users}


@user_routes.route('/<int:id>')
def user(id):
    user = User.query.get(id)
    return user.to_dict() #TODO: add new to_dict method with joined friends and other data

@user_routes.route('/<int:id>/friends')
def get_user_friends(id):
  user = User.query.get(id)

  if user:
    return {'friends': [user.to_dict() for user in user.friends]}
  else:
    return jsonify({'message': 'User could not be found'}), 404
