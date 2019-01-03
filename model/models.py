from app import db

class UserEntity(db.Model):
    __tablename__ = "USER"
    id = db.Column(db.Integer, name='USER_ID', primary_key=True, unique=True)
    name = db.Column(db.String(30), name='USER_NAME', unique=True)
    nick = db.Column(db.String(30), name='USER_NICK', unique=True)
    password = db.Column(db.String(30), name='USER_PASSWORD', unique=True)

    def __init__(self, name, password):
        self.name = name
        self.nick = ''
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.id

class PersonEntity(db.Model):
    __tablename__ = "PERSON"
    id = db.Column(db.Integer, name='PERSON_ID', primary_key=True, unique=True)
    name = db.Column(db.String(30), name='PERSON_NAME', unique=True)
    user = db.Column(db.Integer, name='PERSON_USER', unique=True)
    score = db.Column(db.Integer, name='PERSON_SCORE', unique=True)

    def __init__(self, name, user, score):
        self.name = name
        self.user = user
        self.score = score

    def __repr__(self):
        return '<Person %r>' % self.id


class ItemEntity(db.Model):
    __tablename__ = "ITEMS"
    id = db.Column(db.Integer, name='ITEMS_ID', primary_key=True, unique=True)
    name = db.Column(db.String(30), name='ITEMS_NAME', unique=True)
    score = db.Column(db.Integer, name='ITEMS_SCORE', unique=True)

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return '<Items %r>' % self.id


class PersonItemEntity(db.Model):
    __tablename__ = "PITEMS"
    person = db.Column(db.Integer, name='PITEMS_PERSON', primary_key=True, unique=True)
    item = db.Column(db.Integer, name='PITEMS_ITEM', unique=True)
    times = db.Column(db.Integer, name='PITEMS_TIMES', unique=True)
    score = db.Column(db.Integer, name='PITEMS_SCORE', unique=True)

    def __init__(self, person, item, times, score):
        self.person = person
        self.item = item
        self.times = times
        self.score = score

    def __repr__(self):
        return '<Person Items %r>' % self.person


class HistoryEntity(db.Model):
    __tablename__ = "HISTORY"
    id = db.Column(db.Integer, name='HISTORY_ID', primary_key=True, unique=True)
    person = db.Column(db.Integer, name='HISTORY_PERSON', unique=True)
    type = db.Column(db.Integer, name='HISTORY_TYPE', unique=True)
    item = db.Column(db.Integer, name='HISTORY_ITEM', unique=True)
    score = db.Column(db.Integer, name='HISTORY_SCORE', unique=True)

    def __init__(self, person, type, item, score):
        self.person = person
        self.type = type
        self.item = item
        self.score = score

    def __repr__(self):
        return '<History %r>' % self.id