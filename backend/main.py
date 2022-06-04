from app import app, db, HOST, PORT
from models import *  # DO NOT TOUCH! DB TABLES WILL NOT BE CREATED WITHOUT THIS LINE


def register_routes(app):
    pass


def main():
    register_routes(app)
    db.create_all()
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    main()
