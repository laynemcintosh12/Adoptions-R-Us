from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Database Models"""
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    name = db.Column(db.Text,
                        nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    pic = db.Column(db.Text, 
                        default='https://i.stack.imgur.com/l60Hf.png')
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    avb = db.Column(db.Boolean,
                    default="True")