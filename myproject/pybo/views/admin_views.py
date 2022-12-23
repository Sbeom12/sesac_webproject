# myproject/pybo/views/admin_views.py

from flask import Blueprint, render_template
from ..db import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def question_list():
	cursor = db.cursor()
	sql = "SELECT * FROM question"
	cursor.execute(sql)
	question_list = cursor.fetchall()
	return render_template('question/question_list.html', question_list=question_list)
	# return 'admin_admins.bp - /admin'

@bp.route('/answer')
def index():
	cursor = db.cursor()
	sql = "SELECT * FROM answer"
	cursor.execute(sql)
	answer_list = cursor.fetchall()
	return render_template('answer/answer_list.html', answer_list=answer_list)
	# return 'admin_admins.bp - /admin'
	# return 'admin_admins.bp - /admin/sign'
 
 
