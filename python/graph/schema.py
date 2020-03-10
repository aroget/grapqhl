import graphene

import graph.user.schema
import graph.company.schema


class Query(graph.company.schema.Query, graph.user.schema.Query, graphene.ObjectType):
    pass


class Mutation(graph.company.schema.Mutation, graph.user.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
