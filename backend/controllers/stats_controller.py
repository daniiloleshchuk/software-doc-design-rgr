from flask import jsonify, make_response
from flask_restful import Resource, request
from services import ElectionStatsService


class StatsController(Resource):
    def get(self):
        url_args = request.args
        election_pk = url_args.get('election_pk')
        stats = ElectionStatsService.get_election_stats_by_pk(election_pk=election_pk) if election_pk else dict()
        stats = [{'candidate': candidate, 'total_votes': total_votes} for candidate, total_votes in stats.items()]
        return jsonify(stats) if stats else make_response({'msg': 'Provide election pk please'}, 400)
