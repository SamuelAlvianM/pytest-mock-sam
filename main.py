from flask import Flask
from routes.coffee_service import coffee_blueprint

# untuk membedakan cofiguration dev dengan test kita butuh ini 
def create_app(config_name='development'):

    app = Flask(__name__)

    if config_name == 'development':
        app.config['DEBUG'] = True
    elif config_name == 'testing':
        app.config['TESTING'] = True

    
    app.register_blueprint(coffee_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
