from http import HTTPStatus
from typing import Optional

from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.utils.static_files import load_static_json

bp = Blueprint('core', __name__)


@bp.route('/')
def index():
    return render_template('index.html.jinja')


@bp.route('/lore')
def lore():
    return render_template('lore.html.jinja')


@bp.route('/team')
def team():
    page_data = {
        'users': load_static_json('users.json'),
        'teams': load_static_json('teams.json'),
        'socicons': load_static_json('socicons.json'),
    }

    return render_template('team.html.jinja', **page_data)


@bp.route('/418')
@bp.app_errorhandler(HTTPStatus.IM_A_TEAPOT)
def im_a_teapot(_error: Optional[Exception] = None):
    return render_template('errors/418.html.jinja'), HTTPStatus.IM_A_TEAPOT


@bp.route('/set-lang/<locale>')
def set_language(locale: str):
    session['language'] = locale

    return redirect(request.referrer or url_for('core.index'))
