"""Models for Adoption Agency."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()


class Pet(db.Model):
    """Pet model for Adoption Agency."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """Show info about pet."""

        return (
            f"<Pet("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"species='{self.species}', "
            f"photo_url='{self.photo_url}', "
            f"age={self.age}, "
            f"notes='{self.notes}', "
            f"available={self.available})>"
        )
