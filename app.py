import sqlite3, random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "asdknfrg LSAKFGNfdsak"
app.config["SESSION_COOKIE_NAME"] = "sleS@A!da&sORJ+4"

@app.route("/", methods=["POST", "GET"])
def index():
    session["fruits"], session["shopping_list"] = get_db()
    return render_template("index.html", fruits=session["fruits"],
                                         shopping_list=session["shopping_list"])

@app.route("/add_items", methods=["post"])
def add_items():
    session["shopping_list"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", fruits=session["fruits"],
                                         shopping_list=session["shopping_list"])

@app.route("/remove_items", methods=["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    for item in checked_boxes:
        if item in session["shopping_list"]:
            idx = session["shopping_list"].index(item)
            session["shopping_list"].pop(idx)
            session.modified = True
    return render_template("index.html", fruits=session["fruits"],
                                         shopping_list=session["shopping_list"])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("gyumi.db")
        cursor = db.cursor()
        cursor.execute("SELECT name FROM gyumi")
        all_data = cursor.fetchall()
        fruits = [str(i[0]) for i in all_data]

        shopping_list = fruits.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]

    return fruits, shopping_list

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()