import graphene

import apps.lists.schema


class Query(apps.lists.schema.Query, graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query)
