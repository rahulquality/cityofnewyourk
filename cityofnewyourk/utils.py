import requests
import datetime
from .models import Building as BuildingModel

def fetch_store_buildings(street_name, zip_code):
    try:
        url = 'https://data.cityofnewyork.us/resource/8y4t-faws.json?street_name={street_name}&zip_code={zip_code}'.format(street_name=street_name, zip_code=zip_code)
        res = requests.get(url)
        res_data = res.json()

        for row in res_data:
            row['extracrdt'] = datetime.datetime.fromisoformat(row['extracrdt']).astimezone(datetime.timezone.utc)
            BuildingModel.objects.update_or_create(parid=row['parid'],defaults=row)
    except Exception as e:
        print("errror", e)
        pass