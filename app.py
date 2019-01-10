from flask import Flask, session, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets/scores.sqlite3'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = os.urandom(24) #'PS#yio`%_!((f_or(%)))s'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10) # 配置7天有效
db = SQLAlchemy(app)


from views import item_app, person_app, user_app
app.register_blueprint(user_app, url_prefix='/user')
app.register_blueprint(item_app, url_prefix='/item')
app.register_blueprint(person_app, url_prefix='/person')


@app.before_request
def before_request():
    # 白名单设置,判断为登录页面时
    if request.path == "/user/login":
        return None
    elif session.get("user"):
        return None
    else:
        return redirect(url_for('user.login'))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    session.permanent = True
