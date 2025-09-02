from flask import Blueprint, jsonify

accounting_bp = Blueprint('accounting', __name__)

@accounting_bp.route('/accounting/topics', methods=['GET'])
def get_accounting_topics():
    topics = [
        {"id": 1, "title": "Introduction to Accounting"},
        {"id": 2, "title": "Financial Statements"},
        {"id": 3, "title": "Debits and Credits"},
        {"id": 4, "title": "Accounting Principles"},
        {"id": 5, "title": "Budgeting and Forecasting"},
        {"id": 6, "title": "Taxation"},
        {"id": 7, "title": "Auditing"},
        {"id": 8, "title": "Management Accounting"},
        {"id": 9, "title": "Cost Accounting"},
        {"id": 10, "title": "Accounting Software"}
    ]
    return jsonify(topics)

@accounting_bp.route('/accounting/resources', methods=['GET'])
def get_accounting_resources():
    resources = [
        {"id": 1, "title": "Accounting Basics - Online Course", "link": "https://example.com/accounting-basics"},
        {"id": 2, "title": "Financial Accounting Textbook", "link": "https://example.com/financial-accounting"},
        {"id": 3, "title": "Accounting Principles PDF", "link": "https://example.com/accounting-principles"},
        {"id": 4, "title": "Budgeting Techniques - Video", "link": "https://example.com/budgeting-techniques"},
        {"id": 5, "title": "Taxation Guide", "link": "https://example.com/taxation-guide"}
    ]
    return jsonify(resources)