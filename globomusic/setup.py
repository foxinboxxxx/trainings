from app import create_app, db
from flask_migrate import Migrate

app = create_app()
#SQLalchemy not good at altering table structures
#Render as batch clone DB in background to have new admin column
migrate = Migrate(app, db, render_as_batch=True)
