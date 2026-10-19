import json
import os

from typing import Optional

from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('core', __name__)

# TODO: add Makers page


@bp.route('/')
def index():
    return render_template('index.html.jinja')


@bp.route('/lore')
def lore():
    return render_template('lore.html.jinja')


@bp.route('/team')
def team():

    social_icons = {
        "website": "socicon-internet",
        "twitter": "socicon-twitter",
        "tumblr": "socicon-tumblr",
        "mastodon": "socicon-mastodon",
        "youtube": "socicon-youtube",
        "sketchfab": "socicon-sketchfab",
        "deviantart": "socicon-deviantart",
        "flag": "flag-icon-nl flag-icon",
    }

    user_data = []
    team_data = []

    with open(
        os.path.join(os.path.dirname(__file__), "../static/json/users.json"), 'r'
    ) as file:
        user_data = json.loads(file.read())

    with open(
        os.path.join(os.path.dirname(__file__), "../static/json/teams.json"), 'r'
    ) as file:
        team_data = json.loads(file.read())

    return render_template(
        'team.html.jinja', teams=team_data, users=user_data, socicons=social_icons
    )


@bp.route('/418')
@bp.app_errorhandler(418)
def im_a_teapot(_error: Optional[Exception] = None):
    return render_template('errors/418.html.jinja'), 418


@bp.route('/set-lang/<locale>')
def set_language(locale: str):
    session['language'] = locale

    return redirect(request.referrer or url_for('core.index'))
