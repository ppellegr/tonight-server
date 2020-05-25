import graphene
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .queries import ProfileType, EventType
from ..models import Profile, Event

class ProfileInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    password = graphene.String(required=True)
    max_radius = graphene.Int(required=True)
    email = graphene.String(required=True)

class CreateProfile(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Arguments:
        input = ProfileInput(required=True)

    @staticmethod
    def mutate(root, info, input=None):
        print("info", info)
        print("input", input)
        if not input:
            print("input null")
            return CreateProfile(errors='No input')
        user_instance = get_user_model()(username=input.name, email=input.email)
        user_instance.set_password(input.password)
        user_instance.save()
        profile_instance = Profile(
            user=user_instance,
            event_type=[],
            max_radius=input.max_radius
        )
        profile_instance.save()
        user_group = Group.objects.get(name="basic_users")
        user_group.user_set.add(user_instance)
        return CreateProfile(profile=profile_instance)

class UpdateProfile(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ProfileInput(required=True)

    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, id, input=None):
        profile_instance = Profile.objects.get(pk=id)
        if profile_instance:
            profile_instance.user.username = input.name
            profile_instance.user.email = input.email
            profile_instance.user.password = input.password
            profile_instance.max_radius = input.max_radius
            profile_instance.save()
            return UpdateProfile(profile=profile_instance)
        return UpdateProfile(profile=None)

class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()
    update_profile = UpdateProfile.Field()
