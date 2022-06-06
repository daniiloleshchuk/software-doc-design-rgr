from flask_restful import Api

from app import app, db, HOST, PORT
from models import *  # DO NOT TOUCH! DB TABLES WILL NOT BE CREATED WITHOUT THIS LINE
from controllers import *


def register_routes(app):
    api = Api(app)
    api.add_resource(ElectionController, '/election')
    api.add_resource(ElectionTypeController, '/election_type')
    api.add_resource(OrganizationController, '/organization')
    api.add_resource(RegionController, '/region')
    api.add_resource(UserController, '/user')
    api.add_resource(VoteController, '/vote')


def main():
    register_routes(app)
    db.create_all()
    app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    main()
