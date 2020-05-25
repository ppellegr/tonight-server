from graphene_django.views import GraphQLView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
# from .GraphQL.views import PrivateGraphQLView
from .GraphQL.schema import schema

urlpatterns = [
    path('', views.index),
    path('graphql/', csrf_exempt(GraphQLView.as_view()))
    # path('graphql/', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema)))
    # path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
