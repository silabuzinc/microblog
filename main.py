from flask import render_template, flash, redirect, url_for, request
from flask_login import (
    LoginManager,
    logout_user,
    login_required,
    current_user,
    login_user,
)
from werkzeug.urls import url_parse
from app import create_app
from app.forms import LoginForm
from app.db import db

from app.models.usuarios import AnonymousUser, User
from app.utils.utils import Permission
from app.utils.decorator import admin_required, permission_required


app = create_app()

login = LoginManager(app)
login.login_view = "login"
login.anonymous_user = AnonymousUser


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/")
@login_required
def index():
    return render_template("indexCss.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("no_existe"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        print(type(next_page))
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/no-existe")
def no_existe():
    return render_template("nouser.html")


@app.route("/admin")
@login_required
@admin_required
def for_admins_only():
    return "Para administradores!"


@app.route("/moderate")
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
    return "Para moderadores!"


@app.route("/insert")
def insert():
    u = User(username="marcelo", email="marcelo@mail1.com")
    u.set_password("1301")
    db.session.add(u)
    db.session.commit()
    return "Insertado"


db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()
