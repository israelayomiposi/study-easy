from flask import Blueprint, jsonify

economics_bp = Blueprint('economics', __name__)

# Sample data for economics topics and resources
economics_topics = [
    {
        'id': 1,
        'title': 'Supply and Demand',
        'description': 'Understanding the relationship between supply and demand in economics.',
        'resources': [
            {'type': 'article', 'link': 'https://example.com/supply-demand'},
            {'type': 'video', 'link': 'https://example.com/supply-demand-video'}
        ]
    },
    {
        'id': 2,
        'title': 'Market Structures',
        'description': 'Exploring different types of market structures in economics.',
        'resources': [
            {'type': 'article', 'link': 'https://example.com/market-structures'},
            {'type': 'video', 'link': 'https://example.com/market-structures-video'}
        ]
    }
]

@economics_bp.route('/topics', methods=['GET'])
def get_economics_topics():
    return jsonify(economics_topics)