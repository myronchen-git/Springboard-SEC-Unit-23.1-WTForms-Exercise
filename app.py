"""Adoption Agency"""

from flask import Flask, redirect
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from models import Pet, connect_db, db

# ==================================================


def create_app(db_name, testing=False):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = "secret"
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    if not testing:
        app.config["SQLALCHEMY_ECHO"] = True
    else:
        app.config["SQLALCHEMY_ECHO"] = False

        app.config["TESTING"] = True
        app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

    debug = DebugToolbarExtension(app)

    # --------------------------------------------------

    @app.route("/")
    def root():
        """Root page.  Redirects to /pets."""

        return redirect("/pets")

    @app.route("/pets")
    def homepage():
        """Lists pets."""

        pets = db.session.query(Pet.id, Pet.name, Pet.photo_url,
                                Pet.available).all()

        return render_template("home.html", pets=pets)

    @app.route("/pets/add", methods=["GET"])
    def add_pet():
        """Displays the form to add a pet, and adds a pet."""

        form = AddPetForm()
        
        return render_template("add_pet.html", form=form)

    return app

# ==================================================

if __name__ == "__main__":
    app = create_app("adopt")
    connect_db(app)
    app.run(debug=True)
