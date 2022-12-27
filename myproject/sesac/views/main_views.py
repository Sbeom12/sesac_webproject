# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app, jsonify
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
from datetime import datetime

bp = Blueprint('main_views', __name__, url_prefix='/main')
db = DBUpdater()

# /post/pstId=<int:pstId>
# 특정 게시물로 이동
@bp.route('/')
def grid():

    db = DBUpdater()
    board_ls = db.load_board_list()
    
    post_dict = {}
    for board in board_ls:
        brdId = board['brdId']
        post_dict[brdId] = db.load_post_brdId_list(brdId)[:5]
    
    # 특정 게시물 html 불러오기
    return render_template('pages/main.html', board_ls=board_ls, post_dict=post_dict)


# 게시물 클릭하면 조회수 올리기
@bp.route('/vw', methods=('GET', 'POST'))
def vwFunc():
    # method = POST
    if(request.method == 'POST'):
        # main.html에서 받아온 pstId 저장
        pstId = request.get_json()["pstId"]
        
        # 조회수 +1 한 후 저장
        vwCnt = db.extractWhere("vwCnt", "Post", "pstId", int(pstId))
        vwCnt = vwCnt+1
        db.addVwCnt(vwCnt, pstId)
        
        # pstId return
        return jsonify({'msg': pstId})
    
    # method = GET
    else:
        render_template('pages/main.html')
