# myproject/sesac/__init__.py
from flask import Flask, render_template, session, redirect, url_for, jsonify

from flask import request
from datetime import timedelta
# from flask_wtf import FlaskForm
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# from flask_sqlalchemy import SQLAlchemy

# Blueprint views 불러오기 
from .views import (
	user_views, post_views, board_views, admin_views
)
# flask의 create_app - Flask Application Factory
def create_app():
	print('----------create_app----------')	
	app = Flask(__name__, template_folder='templates')
	app.secret_key = 'secretkey'  # secret_key는 서버상에 동작하는 어플리케이션 구분하기 위해 사용하고 복잡하게 만들어야 합니다.
	app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30) # 로그인 지속시간을 정합니다. 현재 1분


	@app.route('/')
	def main():
		#session['username'] = 'abc'
		print("/",session)
		return render_template('pages/main.html')
		# return '/ - /'


	# Blueprint views를 app에 등록
	app.register_blueprint(user_views.bp)
	app.register_blueprint(post_views.bp)
	app.register_blueprint(board_views.bp)
	app.register_blueprint(admin_views.bp)

	return app

