import os
from flask import Flask
<<<<<<< HEAD

=======
>>>>>>> 3a452056ab996daef6836f956657c8ffba796133
from flask import render_template

def create_app(test_config =None):
        # create & config the app
        app = Flask(__name__ , instance_relative_config =True)
        app.config.from_mapping( SECRET_KEY='dev' , DATABASE = os.path.join(app.instance_path , 'fin.sqlite'))

        if test_config is None:
                # load the instance config, if it exists, when not testing
                app.config.from_pyfile('config.py', silent=True)
        else:
                # load the test config if passed in
                app.config.from_mapping(test_config)

        try:
                os.makedirs(app.instance_path)
        except:
                pass

        @app.route('/home')
        def hello():
                return render_template('home.html')

        from . import db
        db.init_app(app)

<<<<<<< HEAD
        from . import auth 
=======
        from . import auth
>>>>>>> 3a452056ab996daef6836f956657c8ffba796133
        app.register_blueprint(auth.bp)

        
        return app
