from rest_framework.response import Response
from .client.kitsu import KitsuClient
from rest_framework.views import APIView

import json

class QueryParameterParser():
    "Build query paramaters to query kitsu"
    def __init__(self, query):
        self.parsed = False
        self._params = {}
        self.query = query

    def parse(self):
        "Parse parameters to build proper query to kitsu api"
        if not self.parsed:
            for key, value in self.query.items():
                has_json_params = False
                for param in self._paramsList():
                    has_json_params = self.addJsonAPIParam(param, key, value)
                    if (has_json_params):
                        break
                if (not has_json_params):
                    self._params[key] = value
                self.parsed = True
        return self._params

    def _paramsList(self):
        return ['filter', 'page']

    def addJsonAPIParam(self, json_param, key, value):
        "Add param from json api to params"
        if key.find(json_param + '[') == 0 and key.find(']') == len(key) - 1:
            found = True
            json_param_name = key.replace(json_param + '[', '').replace(']', '')
            if not json_param in self._params.keys():
                self._params[json_param] = {}
            self._params[json_param][json_param_name] = value
        else:
            found = False
        return found

class KitsuList(APIView):
    "Base class for kitsu endpoints."
    endpoint = ''
    def getEndpoint(self):
        return self.endpoint

    def get(self, request, format=None):
        parser = QueryParameterParser(request.query_params)
        params = parser.parse()
        client = KitsuClient()
        response = client.get(self.getEndpoint(), params)
        return Response(json.loads(response))

class AnimeList(KitsuList):
    "Anime list endpoint"
    endpoint = 'anime'

class GenresList(KitsuList):
    "Genres list endpoint"
    endpoint = 'genres'


# @TODO: single entities endpoints!

class KitsuEntity(APIView):
    "Base class for kitsu endpoints."
    endpoint = ''
    def getEndpoint(self):
        return self.endpoint

    def get(self, request, pk, format=None):
        parser = QueryParameterParser(request.query_params)
        params = parser.parse()
        client = KitsuClient()
        response = client.get(self.getEndpoint() + '/' + pk, params)
        return Response(json.loads(response))

class AnimeEntity(KitsuEntity):
    "Anime detail endpoint"
    endpoint = 'anime'

class GenresEntity(KitsuEntity):
    "Genre detail endpoint"
    endpoint = 'genres'
