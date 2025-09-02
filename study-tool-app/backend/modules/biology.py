from flask import Blueprint, jsonify

biology_bp = Blueprint('biology', __name__)

@biology_bp.route('/biology/topics', methods=['GET'])
def get_biology_topics():
    topics = [
        {"id": 1, "title": "Cell Biology"},
        {"id": 2, "title": "Genetics"},
        {"id": 3, "title": "Evolution"},
        {"id": 4, "title": "Ecology"},
        {"id": 5, "title": "Human Anatomy"},
        {"id": 6, "title": "Plant Biology"},
        {"id": 7, "title": "Microbiology"},
        {"id": 8, "title": "Biochemistry"},
    ]
    return jsonify(topics)

@biology_bp.route('/biology/resources', methods=['GET'])
def get_biology_resources():
    resources = [
        {"id": 1, "title": "Biology Textbook", "link": "https://example.com/biology-textbook"},
        {"id": 2, "title": "Khan Academy Biology", "link": "https://www.khanacademy.org/science/biology"},
        {"id": 3, "title": "Crash Course Biology", "link": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtP8g8t0g1g0g0g0g0g0g0g"},
    ]
    return jsonify(resources)