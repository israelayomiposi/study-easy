from flask import Blueprint, jsonify

government_bp = Blueprint('government', __name__)

@government_bp.route('/government/topics', methods=['GET'])
def get_government_topics():
    topics = [
        {"id": 1, "title": "Introduction to Government"},
        {"id": 2, "title": "Types of Government"},
        {"id": 3, "title": "The Constitution"},
        {"id": 4, "title": "Branches of Government"},
        {"id": 5, "title": "Checks and Balances"},
        {"id": 6, "title": "Civil Rights and Liberties"},
        {"id": 7, "title": "Political Parties"},
        {"id": 8, "title": "Elections and Voting"},
        {"id": 9, "title": "Public Policy"},
        {"id": 10, "title": "International Relations"}
    ]
    return jsonify(topics)

@government_bp.route('/government/resources', methods=['GET'])
def get_government_resources():
    resources = [
        {"id": 1, "title": "Government 101 - Online Course", "link": "https://example.com/course"},
        {"id": 2, "title": "Understanding the Constitution - eBook", "link": "https://example.com/ebook"},
        {"id": 3, "title": "Civic Education Resources", "link": "https://example.com/civic"},
        {"id": 4, "title": "Political Science Journals", "link": "https://example.com/journals"},
        {"id": 5, "title": "Government Podcasts", "link": "https://example.com/podcasts"}
    ]
    return jsonify(resources)