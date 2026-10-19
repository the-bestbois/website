import json
from http import HTTPStatus
from pathlib import Path

from flask import abort, current_app


def load_static_json(name: str) -> dict | list:
    JSON_FOLDER = Path(current_app.static_folder or '') / 'json'
    try:
        with open(JSON_FOLDER / name, 'r') as file:
            return json.load(file)
    except:  # noqa: E722
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
