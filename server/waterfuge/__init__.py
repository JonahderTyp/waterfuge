import logging
import os
from pathlib import Path

from flask import Flask

from .database.seed import seed_database


def create_app():
    logging.basicConfig(level=logging.INFO)
    logging.info("Creating App")
    print("Creating App")

    INSTANCE_PATH = os.path.abspath(os.path.join(
        os.path.abspath(__path__[0]), "../instance"))

    logging.info(f"Instance Path: {INSTANCE_PATH}")

    app = Flask(__name__, instance_path=INSTANCE_PATH)

    # logging.getLogger("werkzeug").setLevel(logging.WARNING)

    CONFIG_PATH = Path(INSTANCE_PATH) / "config.cfg"

    if CONFIG_PATH.is_file():
        app.config.from_pyfile(str(CONFIG_PATH))
        app.logger.info(f"Loaded Config from {CONFIG_PATH}")
        if app.config.get("DEBUG", False):
            app.logger.debug(f"Config:{str(app.config)}")
    else:
        app.logger.warning(f"No Config File Found at {CONFIG_PATH}")

    print(app.config)
    if not (app.config.get("WERKZEUGLOG", False) or app.config.get("DEBUG", False)):
        logging.getLogger("werkzeug").setLevel(logging.WARNING)

    from .database import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Check if every Table is empty
        NEW_DB = all(db.session.query(table).first()
                     is None for table in db.metadata.sorted_tables)

        if NEW_DB:
            app.logger.info("All tables are empty. Seeding database...")
            seed_database()

    from .site import site
    app.register_blueprint(site)

    return app
