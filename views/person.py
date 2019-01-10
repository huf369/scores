from flask import request, render_template, redirect, url_for, session, jsonify
from app import db
from . import person_app
from model.models import PersonEntity

@person_app.route('list')
def list():
    filters = {'user': session.get('user')}
    persons = PersonEntity.query.filter_by(**filters)
    return render_template('/person/list.html', persons=persons)

@person_app.route('add', methods=['POST',])
def add():
    personname = request.values.get('personname')
    personEntity = PersonEntity(name=personname, user=session.get('user'), score='0')
    db.session.add(personEntity)
    #return redirect(url_for('person.list'))
    rd = db.session.query(PersonEntity).filter(PersonEntity.name==personname).first()
    return jsonify(rd.to_json())


@person_app.route('delete', methods=['GET',])
def delete():
    id = request.values.get('id')
    if id is not None:
        db.session.query(PersonEntity).filter(PersonEntity.id==id).delete()
    return redirect(url_for('person.list'))
