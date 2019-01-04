from flask import request, render_template, redirect, url_for, session
from sqlalchemy import and_
from datetime import timedelta

from app import db
from . import user_app
from model.models import UserEntity


@user_app.route('/sign', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('/user/sign.html')
    else:
        username = request.form.get('username')
        password = request.form.get('userpassword')
        users = {'username': username,  'password ': password}
        userEntity = UserEntity(name=username, password=password)
        db.session.add(userEntity)
        return render_template('/person/list.html', user=users)


@user_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/user/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('userpassword')
        filters = {'name':username, 'password':password}
        #rd = UserEntity.query.filter(and_(UserEntity.name==username, UserEntity.password==password)).first()
        rd = UserEntity.query.filter_by(**filters).first()
        if not rd:
            return render_template('/user/login.html', username= username, existError=True)
        session['user'] = rd.id
        return redirect(url_for('person.list'))