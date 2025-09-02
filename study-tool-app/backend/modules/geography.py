from flask import Blueprint, jsonify

geography_bp = Blueprint('geography', __name__)

@geography_bp.route('/geography/topics', methods=['GET'])
def get_geography_topics():
    topics = [
        "Physical Geography",
        "Human Geography",
        "Geographical Information Systems (GIS)",
        "Cartography",
        "Environmental Geography",
        "Cultural Geography",
        "Economic Geography",
        "Urban Geography",
        "Political Geography",
        "Regional Geography"
    ]
    return jsonify(topics)

@geography_bp.route('/geography/resources', methods=['GET'])
def get_geography_resources():
    resources = [
        {
            "title": "National Geographic",
            "url": "https://www.nationalgeographic.com/"
        },
        {
            "title": "Geography.com",
            "url": "https://www.geography.com/"
        },
        {
            "title": "Khan Academy - Geography",
            "url": "https://www.khanacademy.org/humanities/geography"
        },
        {
            "title": "BBC Bitesize - Geography",
            "url": "https://www.bbc.co.uk/bitesize/subjects/zrw76sg"
        }
    ]
    return jsonify(resources)