from django.core.management.base import BaseCommand
import requests
from capitals.models import Country

class Command(BaseCommand):
    help = 'Populate the Country model with data from an API'

    def handle(self, *args, **options):
        url = 'https://countriesnow.space/api/v0.1/countries/capital'  # Replace with the actual API URL

        response = requests.get(url)
        data = response.json().get('data', [])

        for item in data:
            name = item['name']
            capital = item['capital']
            Country.objects.create(name=name, capital=capital)

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
