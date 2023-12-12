from flask import Flask
from reactpy import component, html
from reactpy_router import route, simple
from reactpy.backend.flask import configure

@component
def router():
    return simple.router(
        route("/h1", h1()),
        route("/h2", h2()),
        route("/h3", h3()),
    )

@component
def h1():
    return html.h1("H1")

@component
def h2():
    return html.h2("H2")

@component
def h3():
    return html.h3("H3")

if __name__ == "__main__":

    app = Flask(__name__)
    configure(app, router)

    app.run(debug = True)