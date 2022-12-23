# myproject/pybo/__init__.py
import config
from flask import Flask

# flask의 create_app - Flask Application Factory
def create_app():
	app = Flask(__name__)
	app.config.from_object(config)

	# Blueprint views 불러오기
	from .views import user_views, admin_views, question_views, answer_views

	# user_views.py에 있는 user.bp를 app에 등록
	app.register_blueprint(user_views.bp)

	# admin_views.py에 있는 user.bp를 app에 등록
	app.register_blueprint(admin_views.bp)
	app.register_blueprint(question_views.bp)
	app.register_blueprint(answer_views.bp)

	return app