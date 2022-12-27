# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app, flash
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
			return redirect(url_for('board_views.board'))

		else:
			print('id가 다름')
			flash("삭제 권한이 없습니다.")
			# 특정 게시물 html 불러오기
			return redirect(url_for('post_views.post', pstId=pstId))
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
	board_ls = db.load_board_list()
    # session의 'username'이 있으면 로그인
	if "username" in session:
		# 세션이 있는 경우
		# 세션에 있는 'username' 값과 특정 게시물의 작성자 ID가 같은지 확인
		if str(session['username']) == str(data[0]['userId']):
			# 특정 게시물 편집 html 불러오기
			return render_template('pages/post.edit.html', post_list=data, board_ls=board_ls)

		else:
			print('id가 다름')
			flash("편집 권한이 없습니다.")
			# 특정 게시물 html 불러오기
			return redirect(url_for('post_views.post', pstId=pstId, board_ls=board_ls))
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
		db =  DBUpdater()
		# 특정 게시물 편집 html 불러오기
		board_ls = db.load_board_list()
		return render_template('pages/post.edit.html', board_ls=board_ls)
	else:
		# 세션이 없는 경우'
		print('First Login')
		return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기! </a>"


# 편집 저장하기 버튼 클릭
@bp.route('/save/<int:pstId>/', methods=('GET', 'POST'))
def post_save_edit(pstId):
    brdId = request.form['brdId']
    db = DBUpdater()
    board_ls = db.load_board_list()
    print(request.form)
    db.update_post(request.form, pstId)
    return redirect(url_for('board_views.board_boardID', brdId=brdId, board_ls=board_ls))


# 작성 저장하기 버튼 클릭
@bp.route('/save/', methods=('GET', 'POST'))
def post_save_new():
	brdId = request.form['brdId']
	userId = session["username"]
	title = request.form['title']
	pstCntnt = request.form['pstCntnt']

	db = DBUpdater()
	db.insertPost(brdId, userId, title, pstCntnt)
	board_ls = db.load_board_list()

	return redirect(url_for('board_views.board_boardID', brdId=brdId))
    # return redirect(url_for('post_views.post', pstId=pstId))
    

# 작성 저장하기 버튼 클릭
@bp.route('/like/<pstId>/<type>/<post>', methods=('GET', 'POST'))
def like_unlike_click(pstId, type, post):
	"""
	Args:
		pstId (_type_): _description_
		type (_type_): like or unlike
		post (int, optional): _description_. Defaults to 1.
	"""
	post = int(post)
	pstId = int(pstId)
	print('like_unlike_click :', pstId, type, post)
	# try:
	if "username" in session:
		# 존재하면 로직 진행
		db = DBUpdater()
		# 해당 게시물에 대한 좋아요 싫어요 row가 있는지 확인
		if db.existence_item(pstId, session['username'], post) == 0:
			# 없으면 insert 기본 값
			db.insert_item(pstId, session['username'], post)

		# 해당 type(like or unlike)이 False 이면 : True로 변경
		# 해당 type이 True 이면 : False로 변경
		db.update_item_type(type, pstId, session['username'], post)

		# 해당 pstId의 sum(like) 값을 Post의 pstLikeCnt으로 업데이트
		id = db.update_pstlikeCnt(type, pstId, post)
		return redirect(url_for('post_views.post', pstId=id))
	else:
		# 세션이 없는 경우'
		print('First Login')
		return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기! </a>"

	return redirect(url_for('board_views.board_boardID', brdId=brdId, board_ls=board_ls))

