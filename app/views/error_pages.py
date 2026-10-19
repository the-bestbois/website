from http import HTTPStatus

from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

bp = Blueprint('error_pages', __name__)


@bp.app_errorhandler(HTTPStatus.NOT_FOUND)
@bp.app_errorhandler(HTTPStatus.IM_A_TEAPOT)
@bp.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def not_found(error):
    code = error.code
    try:
        return render_template(f'errors/{code}.html.jinja'), code
    except TemplateNotFound:
        return str(code)


@bp.app_errorhandler(TemplateNotFound)
def template_not_found(_error):
    return render_template('errors/500.html.jinja')
