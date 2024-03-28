import email
from app.config.db_config import *
import os
import sys
from flask import request, jsonify
from app.models.tables.user import User
from app.models.tables.note import Note
from werkzeug.security import generate_password_hash, check_password_hash


@app.post('/api/add_user')
def add_user():
    try:
        body = request.get_json()
        username = body['name']
        email = body['email']
        password = body['password']
        re_password = body['re_password']

        if password != re_password:
            return jsonify({
                'status': 'Error',
                'message': 'Senhas não coencidem'
            }), 400
        
        password_hash = generate_password_hash(password)

        user = User(username=username, email=email, password_hash=password_hash)

        db.session.add(user)
        db.session.commit()
        db.session.close()

        return jsonify({
            'status': 'ok',
            'message': 'Usuario cadastrado com sucesso'
        }), 201
    
    except Exception as error:
        print(f'error class: {error.__class__} | error cause: {error.__cause__}')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return jsonify({
                'status': 'error',
                'message': 'An error has occurred!',
                'error_class': str(error.__class__),
                'error_cause': str(error.__cause__)
            }), 500


@app.delete('/api/delete_user')
def delete_user():
    try:
        body = request.get_json()
        id_user = body['id']
        user = User.query.filter_by(id=id_user).first()

        if id_user != user.id:
            return jsonify({
                'status': 'Error',
                'message': 'Usuário não encontrado!'
            }), 400
        
        db.session.delete(user)
        db.session.commit()
        db.session.close()

        return jsonify({
            'stutus': 'ok',
            'message': 'Usuario cadastrado com sucesso'
        }), 200
    
    except Exception as error:
        print(f'error class: {error.__class__} | error cause: {error.__cause__}')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return jsonify({
                'status': 'error',
                'message': 'An error has occurred!',
                'error_class': str(error.__class__),
                'error_cause': str(error.__cause__)
            }), 500
    

@app.post('/api/add_note')
def add_note():
    try:
        body = request.get_json()
        note_title = body['title']
        note_content = body['content']
        user = body['id']
        
        if note_title == '' or note_content == '':
            return jsonify({
                'status': 'Error',
                'message': 'Campos não preenchidos!'
            }), 400
        
        new_note = Note(title=note_title, content=note_content, user_id=user)

        db.session.add(new_note)
        db.session.commit()
        db.session.close()

        return jsonify({
            'stutus': 'ok',
            'message': 'Nota adicionada com sucesso'
        }), 200
    
    except Exception as error:
        print(f'error class: {error.__class__} | error cause: {error.__cause__}')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return jsonify({
                'status': 'error',
                'message': 'An error has occurred!',
                'error_class': str(error.__class__),
                'error_cause': str(error.__cause__)
            }), 500




