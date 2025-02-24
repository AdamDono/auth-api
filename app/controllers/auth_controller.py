from flask import jsonify, request, current_app
from app.models.user import User
from app import db

def signup():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(
        username=data.get('username'),
        email=data['email'],
        password=data['password']
    )
    
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating user'}), 500

def login():
    data = request.get_json()
    
    user = User.query.filter_by(email=data.get('email')).first()
    
    if not user or not user.verify_password(data.get('password')):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = user.generate_auth_token()
    return jsonify({'token': token.decode('utf-8')}), 200