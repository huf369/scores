from flask import request, render_template
from . import person_app

@person_app.route('list')
def list():
    persons = [{'id': '1', 'name': '胡天航', 'scores': "100"}, {'id': '1', 'name': '胡天奥', 'scores': "120"}]
    return render_template('/person/list.html', persons=persons)