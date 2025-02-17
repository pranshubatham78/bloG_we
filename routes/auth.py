from flask import render_template, redirect, url_for, flash, request, Blueprint
from forms.auth_Forms import SignupForm, LoginForm, ResetRequestForm, ResetPasswordForm
from models.user import User
from models import db
from app import bcrypt
from . import auth_bp


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm() # load the signup form
    if form.validate_on_submit():
        # Now, We need to hash the password and store it in db
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are able to login', 'success')
        return redirect(url_for('auth.login'))
    return render_template('registration.html', form=form)
