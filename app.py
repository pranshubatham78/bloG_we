from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, init_models
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from routes import create_app


# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Initialize models
with app.app_context():
    init_models()

# Register Blueprints
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
