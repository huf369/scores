from flask import Blueprint

item_app = Blueprint('item', __name__)
user_app = Blueprint('user', __name__)
person_app = Blueprint('person', __name__)


from . import item
from . import person
from . import user