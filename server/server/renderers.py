from rest_framework.renderers import JSONRenderer

class EmberJSONRenderer(JSONRenderer):
    media_type = 'application/vnd.api+json'
