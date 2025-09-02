from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth.routes import auth_bp
from dashboard.routes import dashboard_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_tool.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug=True)