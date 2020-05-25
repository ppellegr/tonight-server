import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import permission_required

from ..models import Profile, Event

from django.contrib.auth.models import Permission

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ('user', 'max_radius', )

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class EventType(DjangoObjectType):
    class Meta:
        model = Event

class Query(ObjectType):
    profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.Int())
    events = graphene.List(EventType)
    event = graphene.Field(EventType, id=graphene.Int())
    event_search = graphene.List(EventType, string=graphene.String())
    me = graphene.Field(UserType)

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Profile.objects.get(pk=id)

        return None

    @permission_required('event.view_event') # https://django-graphql-jwt.domake.io/en/latest/decorators.html
    def resolve_events(self, info, **kwargs):
        print("authenticated:", info.context.user.is_authenticated)
        qs = Event.objects.all()
        skip = kwargs.get('skip')
        first = kwargs.get('first')
        search = kwargs.get('search')
        if skip:
            qs = qs[skip:] #TODO check skip value
        if first:
            qs = qs[:first] #TODO check first value
        return qs

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Event.objects.get(pk=id)

        return None

    def resole_event_search(self, info, **kwargs):
        string = kwargs.get("string", "")
        return Event.object.filter(name__icontains=string)

    def resolve_me(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
