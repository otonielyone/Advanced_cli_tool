from siteopsdashboard.extension.login_manager import login_manager
from siteopsdashboard.extension.ldap_manager import ldap_manager
from siteopsdashboard.models.users.users import User
from siteopsdashboard.models.users.users import db
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from flask_ldap3_login.forms import LDAPLoginForm


auth = Blueprint('auth', __name__)

@ldap_manager.save_user   
def save_user(username):
    username = User.query.filter_by(username=username).first()
    if username != True:
        username = User(username=username)
        db.session.add(username)
        db.session.commit()
        return username

@login_manager.user_loader
def load_user(username):
    username = User.query.filter_by(username=username).first()
    return username


@auth.route('/', methods=['GET','POST'])
def login():
    form = LDAPLoginForm()
    if current_user.is_authenticated:
        return render_template('home.html', user=current_user)
    elif request.method == 'POST':
        req = request.form
        username = req.get("username")
        print(username)
        if username: 
            if form.validate_on_submit():
                login_user(form.username, remember=True)
                flash('user validated', category='success')
            flash('user not validated', category='success')
        return render_template('login.html', user=current_user, form=form)
    return render_template('login.html', user=current_user, form=form)

    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))  