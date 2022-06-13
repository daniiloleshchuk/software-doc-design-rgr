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
    api.add_resource(StatsController, '/stats')


def main():
    register_routes(app)
    db.create_all()
    # region = Region(name="Test")
    # region._save()
    # vova_candidate = User(name='Vova', age=18, region_pk=1, passport_id="Aboba")
    # petia_candidate = User(name='Petia', age=18, region_pk=1, passport_id="Vlad")
    # vasia_voter = User(name='Vasia', age=18, region_pk=1, passport_id="Ila")
    # denis_voter = User(name='Denis', age=18, region_pk=1, passport_id="Zenyk")
    # zenik_voter = User(name='Zenik', age=18, region_pk=1, passport_id="Ilonka")
    # election_type = ElectionType(voter_votes_count=1, votes_cancelable=True)
    # election_type._save()
    # allowed_regions = ElectionTypeAllowedRegions(election_type_pk=election_type.pk, region_pk=region.pk)
    # allowed_regions._save()
    # election = Election(start=datetime.datetime.utcnow(), end=(datetime.datetime.utcnow() + datetime.timedelta(weeks=5)), type_pk=election_type.pk)
    # election.candidates.append(vova_candidate)
    # election.candidates.append(petia_candidate)
    # election.candidates.append(denis_voter)
    # vasia_voter._save()
    # denis_voter._save()
    # zenik_voter._save()
    # election._save()
    app.run(host=HOST, port=HOST)


if __name__ == '__main__':
    main()
