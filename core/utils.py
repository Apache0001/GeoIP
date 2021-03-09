import requests
from random import randint
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from django.contrib.gis.geoip2 import geoip2

YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

# Usando API do YELP para consulta de estabelecimentos.
def yelp_search(keyword=None, location=None,):
    headers = {
        "Authorization": "Bearer "+ settings.YELP_API_KEY
    }
    if keyword and location:
        params = {
            'terms':keyword,
            'location':location
        }
    else:
        params = {
            'terms':None,
            'location': None
        }

    r = requests.get(
            YELP_SEARCH_ENDPOINT,
            headers=headers, 
            params=params
         )

    return r.json()
# Pegando dados do cliente e usando bancos de dados interno para consulta
def get_client_data():
    g = GeoIP2()
    ip = get_random_ip()
    ip_static = '179.158.229.109'
    try:
        return g.city(ip_static)
    except geoip2.errors.AddressNotFoundError:
        return None

# Gerar IP Dinamicamente
def get_random_ip():
    return '.'.join([str(randint(0, 255)) for x in range(4)])