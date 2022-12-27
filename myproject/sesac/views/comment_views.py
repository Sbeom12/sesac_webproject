# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
from datetime import datetime

bp = Blueprint('comment_views', __name__, url_prefix='/comment')

db = DBUpdater()
board_ls = db.load_board_list()

# 댓글 추가
@bp.route('/add/<int:pstId>/', methods=('GET', 'POST'))
def comment_add(pstId):
    print('comment_add(pstId) -', pstId)
    
    # session이 있을 경우
    if session :
        userId = session['userId']
        cmtCntnt = request.form['cmtCntnt']

        # 특정 게시물 html 불러오기
        db = DBUpdater()
        db.insert_comment(pstId , userId, cmtCntnt)
        return redirect(url_for('post_views.post', pstId=pstId, board_ls=board_ls))
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"



# 댓글 삭제
@bp.route('/del/<int:cmtId>/', methods=('GET', 'POST'))
def comment_del(cmtId):
    print('comment_del(cmtId) -', cmtId)
    db = DBUpdater()
    data = db.match_cmtId(cmtId)
    
    # session이 있을 경우
    if session :
		# 세션에 있는 'username' 값과 특정 게시물의 작성자 ID가 같은지 확인
        if str(session['username']) == str(data[0]['userId']):
            # 댓글 삭제
            db.del_comm(cmtId)

        else:
            print('id가 다름')
            # 특정 게시물 html 불러오기
        return redirect(url_for('post_views.post', pstId=data[0]['pstId'], board_ls=board_ls))
    
    return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"