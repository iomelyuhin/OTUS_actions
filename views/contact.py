from flask import Blueprint, render_template

contact_app = Blueprint("contact_app", __name__)


@contact_app.route("/contact")
def contact_page():
    return render_template("contact.html")
