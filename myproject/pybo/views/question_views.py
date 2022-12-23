# myproject/pybo/views/question_views.py

from flask import Blueprint, render_template, url_for, redirect, request
from ..db import db
from pybo.forms import QuestionForm
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')


 
@bp.route('/<int:question_id>/')
def detail_view(question_id):
    # return str(question_id)
	cursor = db.cursor()
 
	sql = f"SELECT * FROM question WHERE id={question_id}"
	cursor.execute(sql)
	detail = cursor.fetchall()
 
	sql = f"SELECT * FROM answer WHERE question_id={question_id}"
	cursor.execute(sql)
	answers = cursor.fetchall()
	return render_template('question/question_detail.html', detail=detail, answers=answers)

# @bp.route('/create/')
# def create():
#     form = QuestionForm()
#     return render_template('question/question_form.html', form=form)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == "POST" and form.validate_on_submit():
        cursor = db.cursor()
        sql = "insert into question (subject, content, create_date) values ('{}','{}','{}')".format(form.subject.data, form.content.data, datetime.now())
        cursor.execute(sql)
        db.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)