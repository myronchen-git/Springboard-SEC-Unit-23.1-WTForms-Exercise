"""Adoption Agency"""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db

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

  return app

# ==================================================

if __name__ == "__main__":
    app = create_app("adopt")
    connect_db(app)
    app.run(debug=True)