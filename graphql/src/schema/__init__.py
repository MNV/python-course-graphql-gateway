from graphene import Schema

from schema.mutation import Mutation
from schema.query import Query

schema = Schema(query=Query, mutation=Mutation)
