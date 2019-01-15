from flask import request, render_template, redirect, url_for, session, jsonify
from app import db
from . import item_app
from model.models import ItemEntity

@item_app.route('list')
def list():
    filters = {'user': session.get('user')}
    items = ItemEntity.query.filter_by(**filters)
    return render_template('/item/list.html', items=items)

@item_app.route('add', methods=['POST',])
def add():
    id = request.values.get('itemid')
    name = request.values.get('itemname')
    score = request.values.get('itemscore')
    if id=='0':
        itemEntity = ItemEntity(name=name, score=score)
        db.session.add(itemEntity)
    else:
        db.session.query(ItemEntity).filter(ItemEntity.id == id).first()

    return jsonify(itemEntity.to_json())


@item_app.route('delete', methods=['GET',])
def delete():
    id = request.values.get('id')
    if id is not None:
        db.session.query(ItemEntity).filter(ItemEntity.id==id).delete()
    return redirect(url_for('person.list'))
