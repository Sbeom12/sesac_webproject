# 파일 실행 파일
# export FLASK_APP=sesac.py

from sesac import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)