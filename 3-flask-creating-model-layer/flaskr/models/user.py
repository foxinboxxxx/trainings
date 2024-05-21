from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.sqla import sqla

class User(sqla.Model):
    id = sqla.Column(sqla.Integer, primary_key=True)
    username = sqla.Column(sqla.Text, nullable=False, unique=True)
    password = sqla.Column(sqla.Text, nullable=False)


    @validates('username', 'password')
    def validate_non_empty(self, key, value):
        if not value:
            raise ValueError(f'{key.capitalize()} is required')
        if key == 'username':
            self.validate_is_unique(key, value, error_message=f'{value} already registered')

        if key == 'password':
            value = generate_password_hash(value)

        return value
    
    def validate_is_unique(self, key, value, error_message=None):
        if (User.query.filter_by(**{key: value}).first() is not None):
            if not error_message:
                error_message = f'{key} must be unique'
            raise ValueError(error_message)

def correct_password(self, plaintext):
    return check_password_hash(self.password, plaintext)