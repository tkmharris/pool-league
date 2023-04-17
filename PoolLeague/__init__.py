import os
from flask import Flask

import random
from PoolLeague.eight_ball import RESPONSES

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'pool_league.sqlite')
    )

    if test_config is None:
        # load the instance config when not testing, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # register the database
    from . import db
    db.init_app(app)

    # silly test page
    @app.route('/8ball')
    def eight_ball():
        return f"Magic eight ball says ... {random.choice(RESPONSES)}"
    
    return app