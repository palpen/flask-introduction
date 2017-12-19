"""Moving the template code to a separate file.

Mixing Python code with HTML is ugly. Templates usually live in their own
location. By default, flask will look up for templates in a 'templates'
directory living in the same path as the application.

Key idea is to separate business from presentation logic. Presentation logic is the front-end stuff dedicate to the presentaiton of the data. In this example, they are stored in index.html. Business logic is concerned with the infrastructure and data management aspects. This is the back-end stuff.
"""

from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Poe"
    return render_template('index.html', library_name=library_name)
