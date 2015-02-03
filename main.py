#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  hzsunshx
# Created: 2015-02-03 14:41

"""
demo google main page
"""

import os
import flask
app = flask.Flask(__name__)

@app.route('/search')
def search():
    query = flask.request.args.get('q')
    words = []
    for c in 'abcdefg':
        words.append(query+c)
    return flask.jsonify({'words': words})

@app.route('/')
def index():
    return flask.render_template('index.html')

def main():
    app.run(host='0.0.0.0', port=os.getenv('PORT') or 8910, debug=True)

if __name__ == '__main__':
    main()
