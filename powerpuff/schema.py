import graphene
from django.conf import settings


class Query:
    version = graphene.String(description='Service version')

    def resolve_version(self, info, **kwargs):
        return settings.VERSION
