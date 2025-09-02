from flask import Blueprint, jsonify

chemistry_bp = Blueprint('chemistry', __name__)

@chemistry_bp.route('/chemistry/topics', methods=['GET'])
def get_chemistry_topics():
    topics = [
        {"id": 1, "title": "Atomic Structure"},
        {"id": 2, "title": "Periodic Table"},
        {"id": 3, "title": "Chemical Bonds"},
        {"id": 4, "title": "Stoichiometry"},
        {"id": 5, "title": "Thermodynamics"},
        {"id": 6, "title": "Kinetics"},
        {"id": 7, "title": "Equilibrium"},
        {"id": 8, "title": "Acids and Bases"},
        {"id": 9, "title": "Organic Chemistry"},
        {"id": 10, "title": "Inorganic Chemistry"}
    ]
    return jsonify(topics)

@chemistry_bp.route('/chemistry/resources', methods=['GET'])
def get_chemistry_resources():
    resources = [
        {"id": 1, "title": "Chemistry Basics", "link": "https://example.com/chemistry-basics"},
        {"id": 2, "title": "Organic Chemistry Study Guide", "link": "https://example.com/organic-chemistry"},
        {"id": 3, "title": "Periodic Table Reference", "link": "https://example.com/periodic-table"},
        {"id": 4, "title": "Stoichiometry Practice", "link": "https://example.com/stoichiometry"},
        {"id": 5, "title": "Thermodynamics Explained", "link": "https://example.com/thermodynamics"}
    ]
    return jsonify(resources)