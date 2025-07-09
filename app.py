from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///btc_mining.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    binance_id = db.Column(db.String(100))
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

class MiningStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    btc_mined = db.Column(db.Float, default=0.0)
    hash_rate = db.Column(db.Float, default=0.0)
    miners_online = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/mining-stats')
def mining_stats():
    # Tạo dữ liệu đào BTC ảo
    stats = MiningStats.query.first()
    if not stats:
        stats = MiningStats()
        db.session.add(stats)
        db.session.commit()
    
    # Cập nhật số liệu ảo
    stats.btc_mined += random.uniform(0.0001, 0.001)
    stats.hash_rate = random.uniform(150, 200)
    stats.miners_online = random.randint(50, 100)
    stats.last_updated = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'btc_mined': round(stats.btc_mined, 8),
        'hash_rate': round(stats.hash_rate, 2),
        'miners_online': stats.miners_online,
        'last_updated': stats.last_updated.strftime('%H:%M:%S')
    })

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        binance_id = request.form.get('binance_id')
        
        if name and email:
            if binance_id:
                # Nếu có nhập ID Binance, báo lỗi
                error = "Chương trình chỉ dành cho tài khoản Binance đăng ký mới. Vui lòng không nhập ID Binance cũ."
                return render_template('register.html', error=error, name=name, email=email, binance_id=binance_id)
            else:
                # Nếu không nhập ID Binance, hiển thị thông báo và chuyển hướng sau 5 giây
                return render_template('register_binance_redirect.html', name=name, email=email)
    
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/api/users')
def get_users():
    users = User.query.filter_by(is_active=True).order_by(User.registered_at.desc()).limit(10).all()
    return jsonify([{
        'name': user.name,
        'registered_at': user.registered_at.strftime('%d/%m/%Y %H:%M'),
        'binance_id': user.binance_id
    } for user in users])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 