from src import app
from src.routes.all_route import auth_bp
from src.routes.default_route import default_bp
from src.config import Config
from gevent.pywsgi import WSGIServer




app.register_blueprint(auth_bp)
app.register_blueprint(default_bp)

if __name__ == '__main__':
    try:
        http_server = WSGIServer(Config.PORT, app)
        print(f"Server running on {Config.PORT}...🚀")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user...🥱")    
    except Exception as e:
        print("Failed to start server...😴",e)    

