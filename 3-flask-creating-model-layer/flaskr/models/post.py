#from flaskr import sqla
from datetime import datetime
from sqlalchemy.orm import validates
from flaskr.sqla import sqla

class Post(sqla.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    author_id = sqla.Column(sqla.Integer, nullable=False)
    created = sqla.Column(sqla.DateTime, nullable=False, default=datetime.utcnow)
    title = sqla.Column(sqla.Text, nullable=False)
    body = sqla.Column(sqla.Text, nullable=False)

    @validates('title', 'body')
    def validate_non_empty(self, key, value):
        if not value:
            raise ValueError(f'{key.capitalize()} is required')
        return value