from flask import render_template, flash, redirect, request, url_for
from __init__ import fl_app
from forms import LoginForm, RegistrationForm, SendForm, UserAreaForm
from db_adapter import DB
# import globals
import os
import datetime

@fl_app.route('/')
@fl_app.route('/index')
def index():
    recs = DB.query("select * from fishing_places")

    names = [];
    lants = [];
    longs = [];
    bases = [];
    for rec in recs:
        names.append(rec[1])
        lants.append(rec[2])
        longs.append(rec[3])
        bases.append(rec)

    return render_template('index.html', names = names, lants=lants, long=longs, bases = bases)

@fl_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        rec = DB.query("select login_user('" + login_form.username.data + "', '" + login_form.password.data + "')")
        if rec[0][0] == -2:
            flash('No such user!')
        elif rec[0][0] == -1:
            flash('Invalid password')
        else:
            # flash('Login ok!')
            # rec = DB.query("select id from users where \"Login\" = " + "'" + login_form.username.data +"'")
            # globals.user_id = rec[0][0]
            # print(globals.user_id)
            return redirect('/user_area')
    return render_template('login.html', title='Sign In', form=login_form)

@fl_app.route('/user_area', methods=['GET', 'POST'])
def user_area():
    userarea_form = UserAreaForm()
    if userarea_form.validate_on_submit():
        # print("select add_place('" + userarea_form.placename.data + "', " + userarea_form.lant.data + ", " +  userarea_form.long.data + ")")
        rec = DB.query("select add_place('" + userarea_form.placename.data + "', " + userarea_form.lant.data + ", " +  userarea_form.long.data + ")")
        if rec[0][0] == 1:
            flash(userarea_form.placename.data + " added!")
            userarea_form.placename.data = ""
            userarea_form.lant.data = ""
            userarea_form.long.data = ""
    return render_template('user_area.html', title='User Area', form=userarea_form)