from flask import session, redirect, url_for, render_template, request
from . import main
import random

@main.route('/')
def index():
    return redirect(url_for('main_views.grid'))

# @main.route('/join', methods=['GET', 'POST'])
# def join_chat():
#     """Login form to enter a room."""
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         session['room'] = form.room.data
#         return redirect(url_for('.chat'))
#     elif request.method == 'GET':
#         form.name.data = session.get('name', '')
#         form.room.data = session.get('room', '')
#     return render_template('index.html', form=form)


@main.route('/chat/<tag>')
def chat(tag='All'):
    """Chat room. The user's name and room must be stored in
    the session."""
    try:
        session['name'] = session['userSubNm']
    except:
        r = random.randrange(1, 1000)
        session['name'] = 'SESAC_' + str(r).zfill(3)
    session['room'] = str(tag)
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('pages/chat.html', name=name, room=room)
