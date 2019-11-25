import graphene
from graphene_django.types import DjangoObjectType

from . import models


class SpecType(DjangoObjectType):

    class Meta:
        model = models.Spec


class CrashTypeType(DjangoObjectType):

    class Meta:
        model = models.CrashType


class Query(object):

    specs = graphene.List(SpecType)
    crash_types = graphene.List(CrashTypeType)

    def resolve_specs(self, *args, **kwargs):
        return models.Spec.objects.all().prefetch_related('crash_types')

    def resolve_crash_types(self, *args, **kwargs):
        return models.CrashType.objects.all().prefetch_related('specs')
