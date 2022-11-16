from graphene_django import DjangoObjectType
import graphene
from .models import Building as BuildingModel
from .utils import fetch_store_buildings

class Building(DjangoObjectType):
    class Meta:
        model = BuildingModel
        fields = ("__all__")

# Query
class Query(graphene.ObjectType):
    buildings = graphene.Field(Building, street_name=graphene.String(required=True), zip_code=graphene.String(required=True))

    def resolve_buildings(self, info, street_name, zip_code):

        fetch_store_buildings(street_name, zip_code)

        return BuildingModel.objects.filter(street_name=street_name, zip_code=zip_code).first()

# Mutation
class BuildingMutation(graphene.Mutation):
    class Arguments:
        street_name = graphene.String(required=True)
        zip_code = graphene.String(required=True)

    building = graphene.Field(Building)

    @classmethod
    def mutate(cls, root, info, street_name, zip_code):
        fetch_store_buildings(street_name, zip_code)

        return_data = BuildingModel.objects.filter(street_name=street_name, zip_code=zip_code).first()
        
        return BuildingMutation(building=return_data)

class Mutation(graphene.ObjectType):
    update_building = BuildingMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)