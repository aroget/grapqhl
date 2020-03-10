import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from graph.database import db_session
from graph.company.model import CompanyModel


class Company(SQLAlchemyObjectType):
    class Meta:
        model = CompanyModel


class CreateCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    company = graphene.Field(lambda: Company)

    def mutate(root, info, name):
        company = CompanyModel(name=name)
        db_session.add(company)
        db_session.commit()
        return CreateCompany(company=company)


class Query(graphene.ObjectType):
    companies = graphene.List(Company)

    def resolve_companies(self, info):
        query = Company.get_query(info)
        return query.all()


class Mutation(graphene.ObjectType):
    create_company = CreateCompany.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
