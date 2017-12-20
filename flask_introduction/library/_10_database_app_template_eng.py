"""
Requirements:
 * A database created with some data about authors inside.
"""
import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


# a common procedure for every view function. Define here to activate for
# for all view functions
# what is g.db? why is it a variable invoking atttribute?
# g: global object that can be used as a shared workspace
# g.db is an attribute that lives in g, which allows us to use the
# thing binded to it (a database connection object) across functions
@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/authors_template_engine.html', authors=authors)
