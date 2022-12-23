# myproject/sesac/views/admin_views.py

from flask import Blueprint, render_template

bp = Blueprint('admin_views', __name__, url_prefix='/admin')

# /admin
@bp.route('/')
def admin():
    return render_template('pages/admin.html')
	# return 'admin_views.bp - /admin/'

# /admin/userinfo
@bp.route('/userinfo')
def admin_userinfo():
    return render_template('pages/admin.userinfo.html')
	# return 'admin_views.bp - /admin/userinfo'

# /admin/boardinfo
@bp.route('/boardinfo')
def admin_boardinfo():
    return render_template('pages/admin.boardinfo.html')
	# return 'admin_views.bp - /admin/boardinfo'

# /admin/postinfo
@bp.route('/postinfo')
def admin_postinfo():
    return render_template('pages/admin.postinfo.html')
	# return 'admin_views.bp - /admin/postinfo'