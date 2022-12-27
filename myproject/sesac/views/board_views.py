# myproject/sesac/views/board_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
bp = Blueprint('board_views', __name__, url_prefix='/board')

# /board
@bp.route('/')
def board():
    print("board()")
    db = DBUpdater()
    
    number= 5
    page = request.args.get('page', type=int, default=1)
    paging = db.pageSelect2(number ,page)
    board_list = db.load_board_list()
    board_ls = db.load_board_list()
    post_list = db.load_post_list()
    post_len= len(post_list)
    post_len2={'count' : len(post_list)}
    ## 최대 페이지 = 전체 게시글수 -1 을 10으로 나눈 몫에 +1
    max_page = (post_len-1) // number +1
    boards={}
    boards['number']= number
    boards['page']= page
    boards['board_list'] = board_list
    boards['postCnt']= post_len2
    boards['post_list']= paging
    boards['max_page']= list(range(1, max_page+1))

    print(boards)
    # 전체 게시판 html 불러오기
    return render_template('pages/board.html', boards=boards, board_ls=board_ls)

# /board/boardId

@bp.route('/brdId=<int:brdId>/', methods=('GET', 'POST'))
def board_boardID(brdId):
    number= 5
    page = request.args.get('page', type=int, default=1)
    """
    Args:
        brdId (int): 게시판 ID
    """
    print('board_boardID(brdId) -', brdId,"\n")
    
    db = DBUpdater()
    # board_list = 전체 게시판 리스트
    board_list = db.load_board_list()
    # data = 특정 게시판의 게시물 리스트
    data = db.eachPageSelect2(number, page, brdId)
    ## 특정 게시판의 카운트수
    cntAll= db.pageCnt(brdId)
    max_page = (cntAll['count'] -1) // number +1
    boards={}
    boards['number']= number
    boards['page']= page
    boards['brdId']= brdId
    boards['board_list']= board_list
    boards['post_list'] = data
    boards['postCnt']= cntAll
    boards['max_page']= list(range(1, max_page+1))
    print('-'*20,boards)
    return render_template('pages/board.html', boards=boards)

@bp.route('/comp/')
def compInfo():
    return render_template('pages/competition.html')
