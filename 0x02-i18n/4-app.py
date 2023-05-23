#!/usr/bin/env python3
"""
 Detect if the incoming request contains locale argument
"""

import re
import babel
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration   """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)


@babel.localeselector
def get_locale():
    """locale function"""
    lang = request.args.get('locale')
    if lang is not None:
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def gettext():
    """get text"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    
