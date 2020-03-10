import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from graph.database import db_session
from graph.user.model import UserModel
from graph.company.schema import Company


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: User)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        company_id = graphene.Int()

    def mutate(root, info, username, email, password, company_id):
        user = UserModel(username=username, email=email,
                         password_hash=password, company_id=company_id)
        db_session.add(user)
        db_session.commit()
        return CreateUser(user=user)


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# schema = graphene.Schema(query=Query)
