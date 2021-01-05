import graphene

import powerpuff.schema as powerpuff


class Query(powerpuff.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
