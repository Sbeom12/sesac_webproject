# myproject/sesac/views/board_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
bp = Blueprint('board_views', __name__, url_prefix='/board')
db = DBUpdater()
# /board
# 모든 게시글이 있는 게시판으로 이동
# 필요 없나???????
@bp.route('/')
def board():
    print("board()")
    board_list = db.load_board_list()
    post_list = db.load_post_list()
    print(board_list)
    print(post_list)
    # 전체 게시판 html 불러오기
    return render_template('pages/board.html', board_list=board_list, post_list=post_list)


# /board/boardId
# 특정 게시판의 이동
@bp.route('/brdId=<int:brdId>/', methods=('GET', 'POST'))
def board_boardID(brdId):
    """
    Args:
        brdId (int): 게시판 ID
    """
    print('board_boardID(brdId) -', brdId)
    
    db = DBUpdater()
    
    # board_list = 전체 게시판 리스트
    board_list = db.load_board_list()
    print(board_list)
    # data = 특정 게시판의 게시물 리스트
    data = db.load_post_brdId_list(brdId)
    print(data)
    
    # 특정 게시판 html 불러오기
    return render_template('pages/board.html', board_list=board_list, post_list=data, brdId=brdId)
