from flask import (
    Flask,
    render_template,
    Markup,
    url_for,
    flash,
    redirect,
    request
)

import requests
import sendgrid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'

def get_list_view_html(product_id, product):
    
    output = ""
    image_url = url_for("static", filename= product["img"])
    shirt_url = url_for("shirt", product_id=product_id)
    output = output + "<li>"
    output = output + '<a href="' + shirt_url + '">'
    output = output + '<img src="' + image_url + '" alt="' + product["name"] + '">'
    output = output + "<p>View Details</p>"
    output = output + "</a>"
    output = output + "</li>"

    return output

products_info = [
    {
        "id": "101",
        "name": "Logo Shirt, Red",
        "img": "shirt-101.jpg",
        "price": 18,
        "paypal": "LNRBY7XSXS5PA",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "102",
        "name": "Mike the Frog Shirt, Black",
        "img": "shirt-102.jpg",
        "price": 20,
        "paypal": "XP8KRXHEXMQ4J",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "103",
        "name": "Mike the Frog Shirt, Blue",
        "img": "shirt-103.jpg",
        "price": 20,
        "paypal": "95C659J3VZGNJ",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "104",
        "name": "Logo Shirt, Green",
        "img": "shirt-104.jpg",
        "price": 18,
        "paypal": "Z5EY4SJN64SLU",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "105",
        "name": "Mike the Frog Shirt, Yellow",
        "img": "shirt-105.jpg",
        "price": 25,
        "paypal": "RYAGP5EWG4V4G",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "106",
        "name": "Logo Shirt, Gray",
        "img": "shirt-106.jpg",
        "price": 20,
        "paypal": "QYHDD4N4SMUKN",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "107",
        "name": "Logo Shirt, Teal",
        "img": "shirt-107.jpg",
        "price": 20,
        "paypal": "RSDD7RPZFPQTQ",
        "sizes": ["Small","Medium","Large"]
    },

    {
        "id": "108",
        "name": "Mike the Frog Shirt, Orange",
        "img": "shirt-108.jpg",
        "price": 25,
        "paypal": "LFRHBPYZKHV4Y",
        "sizes": ["Small","Medium","Large"]
    }
]

@app.route("/")
def index():
    context = {"page_title": "Shirts 4 Mike"}
    counter = 0
    product_data = []
    for product in products_info:
        counter += 1
        if counter < 5:
            product_data.append(Markup(get_list_view_html(product["id"], product)))
    context["product_data"] = product_data
    flash('This site is a demo do not buy anything')
    return render_template("index.html", **context)

@app.route("/shirts")
def shirts():
    context = {"page_title": "Shirts 4 Mike"}
    product_data = []
    for product in products_info:
        product_data.append(Markup(get_list_view_html(product["id"], product)))
    context["product_data"] = product_data
    flash('This site is a demo do not buy anything')
    return render_template("shirts.html", **context)

@app.route("/shirt/<product_id>")
def shirt(product_id):
    context = {"page_title": "Shirts 4 Mike"}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
    context["product"] = my_product
    flash('This site is a demo do not buy anything')
    return render_template("shirt.html", **context)

@app.route("/receipt")
def receipt():
    pass

@app.route("/contact")
def contact():
    context = {"page_title": "Shirts 4 Mike"}
    return render_template("contact.html", **context)

@app.route("/send", methods=['POST'])
def send():
    print request.form
    sendgrid_object = sendgrid.SendGridClient("Ottermad", "OttersR0ck")
    message = sendgrid.Mail()
    sender = request.form["email"]
    subject = request.form["name"]
    body = request.form["message"]
    message.add_to("charlie.thomas@attwoodthomas.net")
    message.set_from(sender)
    message.set_subject(subject)
    message.set_html(body)
    sendgrid_object.send(message)
    flash('Email sent.')
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True)