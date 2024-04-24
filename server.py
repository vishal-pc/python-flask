from src import app
from src.routes.user_route import auth_bp
from src.routes.default_route import default_bp

app.register_blueprint(auth_bp)
app.register_blueprint(default_bp)

if __name__ == '__main__':
        app.run(debug=True, port=8080)

