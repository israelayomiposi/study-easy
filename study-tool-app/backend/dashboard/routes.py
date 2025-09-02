from flask import Blueprint, jsonify, request
from ..models.user import User
from ..database import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/progress', methods=['GET'])
def get_user_progress():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if user:
        # Assuming user has a progress attribute that stores progress data
        return jsonify({'progress': user.progress}), 200
    return jsonify({'message': 'User not found'}), 404

@dashboard_bp.route('/update_progress', methods=['POST'])
def update_user_progress():
    user_id = request.json.get('user_id')
    progress_data = request.json.get('progress')
    user = User.query.get(user_id)
    if user:
        user.progress = progress_data
        db.session.commit()
        return jsonify({'message': 'Progress updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404