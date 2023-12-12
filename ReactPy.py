from flask import Flask
from reactpy import component, html
from reactpy.backend.flask import configure

@component
def h1():
    return html.h1("Hello World!")

app = Flask(__name__)
configure(app, h1)

if __name__ == "__main__": app.run()