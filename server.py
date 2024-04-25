from src import app
from src.routes.all_route import auth_bp
from src.routes.default_route import default_bp
from src.config import Config

app.register_blueprint(auth_bp)
app.register_blueprint(default_bp)

if __name__ == '__main__':
        app.run(debug=False, port=Config.PORT)

