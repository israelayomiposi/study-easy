from flask import Blueprint, jsonify

english_bp = Blueprint('english', __name__)

@english_bp.route('/english/topics', methods=['GET'])
def get_english_topics():
    topics = [
        "Grammar",
        "Literary Devices",
        "Writing Techniques",
        "Reading Comprehension",
        "Vocabulary Development"
    ]
    return jsonify(topics)

@english_bp.route('/english/resources', methods=['GET'])
def get_english_resources():
    resources = [
        {
            "title": "Purdue OWL",
            "url": "https://owl.purdue.edu/"
        },
        {
            "title": "Grammarly",
            "url": "https://www.grammarly.com/"
        },
        {
            "title": "Khan Academy - English",
            "url": "https://www.khanacademy.org/ela"
        }
    ]
    return jsonify(resources)