# myproject/sesac/views/post_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
from datetime import datetime

bp = Blueprint('main_views', __name__, url_prefix='/main')


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
    #     print(brdId, post_dict[brdId])
    # print(post_dict)

    # 특정 게시물 html 불러오기
    return render_template('pages/main.html', board_ls=board_ls, post_dict=post_dict)