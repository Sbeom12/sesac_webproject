# myproject/sesac/views/info_views.py
from flask import Flask, url_for, request, session, redirect, app
from flask import Blueprint, render_template
from ..sqlModule import DBUpdater
bp = Blueprint('info_views', __name__, url_prefix='/info')

@bp.route('/')
def info():
    print('info')
    return render_template('pages/information.html')