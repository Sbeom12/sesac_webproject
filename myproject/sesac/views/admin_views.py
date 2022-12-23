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
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            userinfo = db.exetractJson('UserInfo')
            return render_template('pages/admin.userinfo.html', userinfo=userinfo)
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/userinfo'


@bp.route('/userinfo/del/<userId>', methods=('GET','POST'))
def userinfo_del(userId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            userinfo = db.deleteUserInfo(userId)
            return redirect(url_for('admin_views.admin_userinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"

@bp.route('/userinfo/grade/<userId>/', methods=('GET','POST'))
def userinfo_grade(userId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            db.update_grade(userId)
            return redirect(url_for('admin_views.admin_userinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"



# /admin/boardinfo
@bp.route('/boardinfo')
def admin_boardinfo():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            
            db = DBUpdater()
            BoardInfo = db.exetractJson('Board')
            return render_template('pages/admin.boardinfo.html', BoardInfo=BoardInfo)
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/boardinfo'



@bp.route('/boardinfo/del/<brdId>', methods=('GET','POST'))
def boardinfo_del(brdId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            userinfo = db.deleteBoard(brdId)
            return redirect(url_for('admin_views.admin_boardinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"

@bp.route('/boardinfo/add', methods=('GET','POST'))
def boardinfo_add():
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            brdNm = request.form['brdNm']
            
            db = DBUpdater()
            db.insertBoard(brdNm, 0)
            return redirect(url_for('admin_views.admin_boardinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"

@bp.route('/boardinfo/edit/<brdId>/', methods=('GET','POST'))
def boardinfo_edit(brdId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            brdNm = request.form['brdNm']
            db = DBUpdater()
            db.update_brdNm(brdId, brdNm)
            return redirect(url_for('admin_views.admin_boardinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"



# /admin/postinfo
@bp.route('/postinfo')
def admin_postinfo():
    db = DBUpdater()
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            PostInfo = db.exetractJson('Post')
            return render_template('pages/admin.postinfo.html', PostInfo=PostInfo)
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/postinfo'


@bp.route('/postinfo/del/<pstId>', methods=('GET','POST'))
def postinfo_del(pstId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            db.deletePost(pstId)
            return redirect(url_for('admin_views.admin_postinfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"



@bp.route('/comminfo')
def admin_comminfo():
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            CommentInfo = db.exetractJson('Comment')
            return render_template('pages/admin.comminfo.html', CommentInfo=CommentInfo)
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
	# return 'admin_views.bp - /admin/boardinfo'

@bp.route('/comminfo/del/<cmtId>', methods=('GET','POST'))
def comminfo_del(cmtId):
    # session이 있을 경우
    if session :
        # 관리자일 경우에 만
        if session['grade'] == 0:
            db = DBUpdater()
            db.deleteComment(cmtId)
            return redirect(url_for('admin_views.admin_comminfo'))
        else:
            return '관리자 권한이 없어요'
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"