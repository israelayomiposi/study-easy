from flask import Blueprint, jsonify

physics_bp = Blueprint('physics', __name__)

@physics_bp.route('/physics/topics', methods=['GET'])
def get_physics_topics():
    topics = [
        {"id": 1, "title": "Kinematics"},
        {"id": 2, "title": "Dynamics"},
        {"id": 3, "title": "Energy"},
        {"id": 4, "title": "Waves"},
        {"id": 5, "title": "Thermodynamics"},
        {"id": 6, "title": "Electromagnetism"},
        {"id": 7, "title": "Optics"},
        {"id": 8, "title": "Modern Physics"}
    ]
    return jsonify(topics)

@physics_bp.route('/physics/resources', methods=['GET'])
def get_physics_resources():
    resources = [
        {"id": 1, "title": "Physics for Beginners", "link": "https://example.com/physics-beginners"},
        {"id": 2, "title": "Advanced Physics", "link": "https://example.com/advanced-physics"},
        {"id": 3, "title": "Physics Experiments", "link": "https://example.com/physics-experiments"},
        {"id": 4, "title": "Physics Simulations", "link": "https://example.com/physics-simulations"}
    ]
    return jsonify(resources)