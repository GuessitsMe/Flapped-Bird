import os
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__, static_folder='.')
CORS(app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


with app.app_context():
    db.create_all()


@app.route('/')
def serve_game():
    return send_from_directory('.', 'index.html')


@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    scores = Score.query.order_by(Score.score.desc()).limit(10).all()
    return jsonify([[s.name, s.score] for s in scores])


@app.route('/api/leaderboard', methods=['POST'])
def submit_score():
    try:
        data = request.get_json(force=True)
        name = data.get('name', '').strip()
        score_value = data.get('score', 0)
        
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        
        new_score = Score(name=name, score=score_value)
        db.session.add(new_score)
        db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
