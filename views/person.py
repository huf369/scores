from flask import request, render_template, redirect, url_for, session
from app import db
from . import person_app
from model.models import PersonEntity

@person_app.route('list')
def list():
    persons = [{'id': '1', 'name': '胡天航', 'scores': "100"}, {'id': '1', 'name': '胡天奥', 'scores': "120"}]
    filters = {'user': session.get('user')}
    persons = PersonEntity.query.filter_by(**filters)
    return render_template('/person/list.html', persons=persons)

@person_app.route('add', methods=['POST',])
def add():
    personname = request.form.get('personname')
    personEntiry = PersonEntity(name=personname, user=session.get('user'), score='0')
    db.session.add(personEntiry)
    return redirect(url_for('person.list'))
