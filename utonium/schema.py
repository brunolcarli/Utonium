import graphene

import powerpuff.schema as powerpuff


class Query(powerpuff.Query, graphene.ObjectType):
    pass


class Mutation(powerpuff.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
