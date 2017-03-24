from rest_framework.parsers import JSONParser

class EmberJSONParser(JSONParser):
    media_type = 'application/vnd.api+json'
