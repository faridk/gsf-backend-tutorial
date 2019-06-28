from db.models import User as UserModel
from gql.resolvers import login as resolve_login
from gql.resolvers import signup as resolve_signup
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
import random
import string


class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    # Return values
    response = graphene.String()

    def mutate(root, info, email, password):
        return Login(response=resolve_login(email, password))


class Signup(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    # Return values
    response = graphene.String()

    def mutate(root, info, email, password):
        return Signup(response=resolve_signup(email, password))


class User(graphene.ObjectType):
    email = graphene.String()
    password = graphene.String()


class MyMutations(graphene.ObjectType):
    login = Login.Field()
    signup = Signup.Field()


# We must define a query for our schema
class MyQueries(graphene.ObjectType):
    user = graphene.Field(User)


schema = graphene.Schema(query=MyQueries, mutation=MyMutations, types=[User])