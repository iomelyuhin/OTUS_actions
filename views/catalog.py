from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest

catalog_app = Blueprint("catalog_app", __name__)


def get_default_products():
    return {
        1: "Развивающие книги",
        2: "Конструкторы",
        3: "Раскраски"
    }


PRODUCTS = get_default_products()


@catalog_app.route("/catalog")
def catalog_list():
    return render_template("catalog/index.html", products=PRODUCTS)


@catalog_app.route("/<int:product_id>/", methods=['GET', 'DELETE'])
def product_detail(product_id: int):
    try:
        product_name = PRODUCTS[product_id]
    except KeyError:
        raise BadRequest(f"Invalid product id #{product_id}")

    if request.method == 'DELETE':
        PRODUCTS.pop(product_id)
        return jsonify(ok=True)

    return render_template(
        "catalog/detail.html",
        product_id=product_id,
        product_name=product_name
    )

#test

@catalog_app.route("/recover/", methods=["POST"])
def recover_products():
    PRODUCTS.update(get_default_products())
    return jsonify(ok=True)
