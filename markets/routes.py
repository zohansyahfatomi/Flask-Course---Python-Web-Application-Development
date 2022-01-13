from markets import app
from flask import render_template, redirect, url_for, flash
from markets.models import Item, User
from markets.form import RegisterForm, LoginForm
from markets import db

@app.route('/') #decorators
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}: #if there not errors from the validation
        for err_msg in form.errors.values():
            flash(f'There are an error: {err_msg}',category='danger')

    return render_template('register.html', form = form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
