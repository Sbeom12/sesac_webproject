# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
from datetime import datetime

bp = Blueprint('post_views', __name__, url_prefix='/post')

db = DBUpdater()
board_ls = db.load_board_list()


# /post/pstId=<int:pstId>
# 특정 게시물로 이동
@bp.route('/pstId=<int:pstId>')
def post(pstId):
	"""
	Args:
		pstId (int): 게시물 ID
	"""
	print('post(pstId) ------', pstId) # pstId가 어떻게 전달이 되는거지,,?

    # data = 특정 게시물 ID 필터링
	db = DBUpdater()
	data = db.load_post_pstId_list(pstId)
	comment_list = db.load_comm_pstId_list(pstId)
 
	board_ls = db.load_board_list()

	# 특정 게시물 html 불러오기
	return render_template('pages/post.html', post_list=data, comment_list=comment_list, board_ls=board_ls)


# /post/del/pstId=<int:pstId>
# 특정 게시물 편집하기
@bp.route('/del/pstId=<int:pstId>', methods=('GET', 'POST'))
def post_del(pstId):
	print('post_del(pstId) -', pstId)

    # data = 특정 게시물 ID 필터링
	db = DBUpdater()
	data = db.load_post_pstId_list(pstId)
	board_ls = db.load_board_list()
 
	print(data)
    # session의 'username'이 있으면 로그인
	if "username" in session:
		# 세션이 있는 경우
		# 세션에 있는 'username' 값과 특정 게시물의 작성자 ID가 같은지 확인
		if str(session['username']) == str(data[0]['userId']):
			
			db.del_post(pstId)
			# 특정 게시물 편집 html 불러오기
			return redirect(url_for('board_views.board'), board_ls=board_ls)

		else:
			print('id가 다름')
			# 특정 게시물 html 불러오기
			return redirect(url_for('post_views.post', pstId=pstId), board_ls=board_ls)
	else:
		# 세션이 없는 경우
		print('First Login')
		return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기! </a>"


# /post/edit/pstId=<int:pstId>
# 특정 게시물 편집하기
@bp.route('/edit/pstId=<int:pstId>', methods=('GET', 'POST'))
def post_edit(pstId):
    
	print('post_edit(pstId) -', pstId)
    
    # data = 특정 게시물 ID 필터링
	db = DBUpdater()
	board_ls = db.load_board_list()
	data = db.load_post_pstId_list(pstId)
	print(data)
    # session의 'username'이 있으면 로그인
	if "username" in session:
		# 세션이 있는 경우
		# 세션에 있는 'username' 값과 특정 게시물의 작성자 ID가 같은지 확인
		if str(session['username']) == str(data[0]['userId']):
			# 특정 게시물 편집 html 불러오기
			return render_template('pages/post.edit.html', post_list=data, board_ls=board_ls)

		else:
			print('id가 다름')
			# 특정 게시물 html 불러오기
			return redirect(url_for('post_views.post', pstId=pstId), board_ls=board_ls)
			# return render_template('pages/post.html', post_list=data)
	else:
		# 세션이 없는 경우
		print('First Login')
		return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기! </a>"



# /post/write
# 작성하기 버튼 클릭
# 게시물 새로 작성하기
@bp.route('/write', methods=('POST', 'GET'))
def post_write():
	print("post_write()")
	db = DBUpdater()
	board_ls = db.load_board_list()
	# session의 'username'이 있으면 로그인
	if "username" in session: 	
		# 세션이 있는 경우

		# 특정 게시물 편집 html 불러오기
		return render_template('pages/post.edit.html', board_ls=board_ls)
	else:
		# 세션이 없는 경우
		print('First Login')
		return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기! </a>"


# 편집 저장하기 버튼 클릭
@bp.route('/save/<int:pstId>/', methods=('GET', 'POST'))
def post_save_edit(pstId):
    brdId = request.form['reg_id']
    db = DBUpdater()
    board_ls = db.load_board_list()
    print(request.form)
    db.update_post(request.form, pstId)
    return redirect(url_for('board_views.board_boardID', brdId=brdId, board_ls=board_ls))


# 작성 저장하기 버튼 클릭
@bp.route('/save//', methods=('GET', 'POST'))
def post_save_new():
	brdId = request.form['reg_id']
	userId = session["username"]
	title = request.form['title']
	pstCntnt = request.form['content']

	db = DBUpdater()
	db.insertPost(brdId, userId, title, pstCntnt)
	board_ls = db.load_board_list()


	return redirect(url_for('board_views.board_boardID', brdId=brdId, board_ls=board_ls))
