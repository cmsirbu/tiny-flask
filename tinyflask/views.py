from tinyflask import app
from tinyflask.config import *

from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', globals=app_globals)
