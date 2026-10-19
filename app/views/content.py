from http import HTTPStatus

from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

# from .avatar_data import AVATAR_DATA

bp = Blueprint('content', __name__)


@bp.route('/worlds/')
def worlds():
    return render_template('worlds.html.jinja')


@bp.route('/models/')
def models():
    return render_template('models.html.jinja')


@bp.route('/models/<avatar_type>')
def avatar(avatar_type: str):
    try:
        return render_template(f'avatars/avatar-{avatar_type}.html.jinja')
    except TemplateNotFound:
        abort(HTTPStatus.NOT_FOUND)


# WIP: dynamic avatar content
# @bp.route('/models/<avatar_type>')
# def avatar(avatar_type: str):
#     if avatar_type not in AVATAR_DATA:
#         abort(HTTPStatus.NOT_FOUND)

#     return render_template('avatar.html.jinja', **AVATAR_DATA[avatar_type])


# @content.route('/clothing')
# def clothing():
#     return render_template('clothing.html.jinja')
