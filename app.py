from flask import Flask, request, render_template

from views import index_app
from views import catalog_app
from views import contact_app

app = Flask(__name__)
app.register_blueprint(index_app)
app.register_blueprint(catalog_app)
app.register_blueprint(contact_app)


@app.route("/", methods=["GET", "POST"])
def index():
    name = "World"
    if request.method == "POST":
        name = request.form.get('name', 'World')
    return render_template("index.html", name=name)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


# @app.route("/catalog", methods=["GET", "POST"])
# def catalog():
#     return f"<h1>Catalog</h1>"
