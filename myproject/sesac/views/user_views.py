# myproject/sesac/views/user_views.py
from flask import Blueprint, render_template
from flask import Flask, url_for, request, session, redirect, app, make_response, flash, g

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from ..sqlModule import DBUpdater

bp = Blueprint('user_views', __name__, url_prefix='/user')


# User 회원가입 (/user/signup)
@bp.route('/signup', methods=('GET', 'POST'))
def user_signup():
    # pages/user.signup.html에서 method POST로 정보가 수신된 경우
    if(request.method == 'POST'):
        
        # form으로 받아온 정보 저장 
        result = request.form.to_dict()
        print(result)
        
        userId = result['userId']
        tel = result['tel']
        email = result['email']
        subNm = result['subNm']
        
        # 이미 존재하는 date인지 확인하기 위해 db에서 date 출력
        db = DBUpdater()
        newUserId = db.extractWhere("userId", "UserInfo", "userId", result['userId'])
        newTel = db.extractWhere("tel", "UserInfo", "tel", result['tel'])
        newEmail = db.extractWhere("email", "UserInfo", "email", result['email'])
        newSubNm = db.extractWhere("subNm", "UserInfo", "subNm", result['subNm'])
        # 만약 기존에 있는 정보라면 다시 signup page 반환
            # ! : 기존에 있었던 정보인지 user에게 알려줄 방법_ flash로 성공
        if(subNm==newSubNm):
            print("이미 존재하는 subNm 입니다.")
            flash("이미 존재하는 subNm 입니다. 다시 입력해주세요.")
            return render_template('pages/user.signup.html')
        elif(userId==newUserId):
            print("이미 존재하는 userId 입니다.")
            flash("이미 존재하는 userId 입니다. 다시 입력해주세요.")
            return render_template('pages/user.signup.html')
        elif (tel==newTel):
            print("이미 존재하는 tel 입니다.")
            flash("이미 존재하는 tel 입니다. 다시 입력해주세요.")
            return render_template('pages/user.signup.html')
        elif(email==newEmail):
            print("이미 존재하는 email 입니다.")
            flash("이미 존재하는 email 입니다. 다시 입력해주세요.")
            return render_template('pages/user.signup.html')
        
        # 기존에 있는 정보가 아니라면 userInfo에 저장 후 login page 반환
            # ! : 회원가입이 완료됐음을 알려줄 방법_ 
        else:
            # userPw는 generate_password_hash()로 암호화해서 저장
            db.insertUserInfo(result['userId'], generate_password_hash(result['userPw']), result['userNm'], result['subNm'] , result['tel'], result['email'])
            return render_template('pages/user.login.html')
    
    # pages/user.signup.html에서 method GET으로 정보가 수신된 경우
    else:
        # 다시 pages/user.signup.html 반환
        return render_template('pages/user.signup.html')

################################################################################################################################################

# 로그인 (/user/login)
@bp.route('/login', methods=('GET', 'POST'))
def user_login():
    
    # pages/user.login.html에서 method POST로 정보가 수신된 경우
    if(request.method == 'POST'):
        # form으로 받아온 정보 저장 
        result = request.form.to_dict()
        print(result["userId"], result["userPw"])
        
        # 수신된 정보 존재 확인 및 ID&PW 매칭
        db = DBUpdater()
        userPw = db.extractWhere("userPw", "UserInfo", "userId", result['userId'])
        userNm = db.extractWhere("userNm", "UserInfo", "userId", result['userId'])
        userSubNm = db.extractWhere("subNm", "UserInfo", "userId", result['userId'])
        grade = db.extractWhere("grade", "UserInfo", "userId", result['userId'])
        
            # 정보가 일치하는 경우 userId를 session에 저장 후 page/main.html 반환
        if(check_password_hash(userPw, result["userPw"])):  # check_password_hash()로 복호화해서 확인
            print("정보가 일치합니다. 로그인 성공 !")
            
            # 추후에 게시물 작성할 때 필요한 session 정보 저장
            session['userId'] = request.form['userId']
            session['userNm'] = userNm
            session['userSubNm'] = userSubNm
            session['username'] = request.form['userId']
            session['grade'] = grade
            
            print("User Session: ", session)
            return redirect(url_for('main'))
        
            # 없는 정보거나 정보가 일치하지 않을 경우 다시 pages/user.login.html 반환
        else:
            print("정보가 일치하지 않습니다. 올바르게 입력해주세요")
            flash("정보가 일치하지 않습니다. 올바르게 입력해주세요")
            return render_template('pages/user.login.html')
        
    # pages/user.login.html에서 method GET으로 정보가 수신된 경우
    else:
        return render_template('pages/user.login.html')
    
################################################################################################################################################

# 로그아웃(/user/logout)
@bp.route('/logout')
def user_logout():
    
    # session에 userId가 존재하면 userId 제거
    if("userId" in session):
        # session.pop('userId', None)
        session.clear()
        print(session) 
    # session에 userId가 존재하지 않으면 session 출력해 확인
    else:
        print(session) 
    # pages/main.html 반환
    return redirect(url_for('main'))

################################################################################################################################################

# 마이페이지(/user/mypage)
@bp.route('/mypage')
def user_mypage():    
    # data는 유저 아이디랑 일치하는 모든 게시물과 댓글
    # session에 userId가 있는 경우
    if 'userId' in session:
        db = DBUpdater()
        post_list = db.load_post_userId_list(session['userId'])
        comm_list = db.load_comm_userId_list(session['userId'])
        
        return render_template('pages/user.mypage.html', post_list=post_list, comm_list=comm_list)
    else:
        # session에 'userId'가 없으면 pages/user.login.html 반환
        return "로그인 해주세요. <br><a href = '/user/login'> 로그인 하러가기 </a>"
    
################################################################################################################################################