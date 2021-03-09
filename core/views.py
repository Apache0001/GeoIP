from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        items = []
        city =  None
        q = request.GET.get('key',default=None)
        loc =  request.GET.get('loc',default=None)
        print(q)
        print(loc)
        items = yelp_search(keyword=q, location=loc)
        context = {
            'items': items,
            'city': loc,
            'busca': True
        }
        print(items)

        return render(request, 'index.html', context)