# myproject/pybo/views/user_views.py

from flask import Blueprint
from ..db import db

bp = Blueprint('detail', __name__, url_prefix='/detail')

@bp.route('/')
def user_main():
    # return str(question_id)
	cursor = db.cursor()
 
	sql = f"SELECT * FROM Board"
	cursor.execute(sql)
	detail = cursor.fetchall()
	return str()

@bp.route('/sign')
def user_sign():
	return 'user_views.bp - /user/sign'

