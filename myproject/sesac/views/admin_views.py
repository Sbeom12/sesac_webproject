# myproject/sesac/views/admin_views.py
from flask import Blueprint, render_template
from flask import Flask, url_for, request, session, redirect, app, make_response, flash, g

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from ..sqlModule import DBUpdater

bp = Blueprint('admin_views', __name__, url_prefix='/admin')

# /admin
@bp.route('/')
def admin():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            return render_template('pages/admin.html')
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/'

# /admin/userinfo
@bp.route('/userinfo')
def admin_userinfo():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            return render_template('pages/admin.userinfo.html')
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/userinfo'

# /admin/boardinfo
@bp.route('/boardinfo')
def admin_boardinfo():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            return render_template('pages/admin.boardinfo.html')
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/boardinfo'

# /admin/postinfo
@bp.route('/postinfo')
def admin_postinfo():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            return render_template('pages/admin.postinfo.html')
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/postinfo'