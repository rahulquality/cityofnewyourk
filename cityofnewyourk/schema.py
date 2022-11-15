from graphene_django import DjangoObjectType
import graphene
from .models import Building as BuildingModel
from .utils import fetch_store_buildings

class Building(DjangoObjectType):
    class Meta:
        model = BuildingModel
        fields = ("__all__")

class Query(graphene.ObjectType):
    buildings = graphene.List(Building, street_name=graphene.String(required=True), zip_code=graphene.String(required=True))

    def resolve_buildings(self, info, street_name, zip_code):

        fetch_store_buildings(street_name, zip_code)

        return BuildingModel.objects.filter(street_name=street_name, zip_code=zip_code).all()

schema = graphene.Schema(query=Query)