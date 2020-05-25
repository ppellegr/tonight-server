from graphene import ObjectType, Schema
from graphene_django.debug import DjangoDebug
import graphene

from event.GraphQL.schema import Query as InfoQuery
from event.GraphQL.schema import Mutation as InfoMutation

import graphql_jwt

class Query(InfoQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(InfoMutation, ObjectType):
    # This class will inherit from multiple Mutations
    # as we begin to add more apps to our project
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = Schema(query=Query, mutation=Mutation)
