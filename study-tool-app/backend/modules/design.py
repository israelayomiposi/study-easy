from flask import Blueprint, jsonify

design_bp = Blueprint('design', __name__)

@design_bp.route('/design/topics', methods=['GET'])
def get_design_topics():
    topics = [
        {"id": 1, "title": "Introduction to Design"},
        {"id": 2, "title": "Principles of Design"},
        {"id": 3, "title": "Color Theory"},
        {"id": 4, "title": "Typography"},
        {"id": 5, "title": "User Experience Design"},
        {"id": 6, "title": "Graphic Design Tools"},
        {"id": 7, "title": "Design Thinking"},
        {"id": 8, "title": "Branding and Identity"},
        {"id": 9, "title": "Web Design Basics"},
        {"id": 10, "title": "Portfolio Development"}
    ]
    return jsonify(topics)

@design_bp.route('/design/resources', methods=['GET'])
def get_design_resources():
    resources = [
        {"id": 1, "title": "The Design of Everyday Things", "link": "https://www.example.com/design-of-everyday-things"},
        {"id": 2, "title": "Don't Make Me Think", "link": "https://www.example.com/dont-make-me-think"},
        {"id": 3, "title": "Adobe Creative Cloud", "link": "https://www.adobe.com/creativecloud.html"},
        {"id": 4, "title": "Canva", "link": "https://www.canva.com"},
        {"id": 5, "title": "Figma", "link": "https://www.figma.com"},
        {"id": 6, "title": "Skillshare Design Courses", "link": "https://www.skillshare.com/browse/design"},
        {"id": 7, "title": "Coursera Design Specializations", "link": "https://www.coursera.org/browse/business/design"},
        {"id": 8, "title": "YouTube Design Tutorials", "link": "https://www.youtube.com/results?search_query=design+tutorials"}
    ]
    return jsonify(resources)