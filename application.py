from flask import Flask, render_template, request, redirect, url_for
import sys
import database
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("hello.html")


@application.route("/apply")
def apply():
    return render_template("apply.html")

@application.route("/applyphoto")
def photo():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True
    database.save(location, cleaness, built_in)
    return render_template("applyphoto.html")
    
@application.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("hello"))

@application.route("/list")
def list():
    house_list = database.load_list()
    length = len(house_list)
    return render_template("list.html", house_list = house_list, length=length)


if __name__ == "__main__":
    application.run(host='0.0.0.0', )
