import datetime

from flask_restful import Api

from app import app, db, HOST, PORT
from models import *  # DO NOT TOUCH! DB TABLES WILL NOT BE CREATED WITHOUT THIS LINE
from controllers import *


def register_routes(app):
    api = Api(app)
    api.add_resource(ElectionController, '/election')
    api.add_resource(ElectionTypeController, '/election_type')
    api.add_resource(RegionController, '/region')
    api.add_resource(UserController, '/user')
    api.add_resource(VoteController, '/vote')


def main():
    register_routes(app)
    db.create_all()
    # vova_candidate = User(name='Vova')
    # petia_candidate = User(name='Petia')
    # vasia_voter = User(name='Vasia')
    # denis_voter = User(name='Denis')
    # zenik_voter = User(name='Zenik')
    # election_type = ElectionType()
    # election = Election(type=election_type, start=datetime.datetime.now(), end=datetime.datetime.now())
    # election.candidates.append(vova_candidate)
    # election.candidates.append(petia_candidate)
    # election._save()
    # vasia_voter._save()
    # denis_voter._save()
    # zenik_voter._save()
    app.run(host=HOST, port=HOST)


if __name__ == '__main__':
    main()
