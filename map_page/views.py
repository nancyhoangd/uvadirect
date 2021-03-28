from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def map_page(request):
    return HttpResponse("Maps display page")
    
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': 'pk.eyJ1IjoibWFwcHJvamVjdDMyNDAiLCJhIjoiY2ttdHBzMWJuMGYwcjJ2cGRxaXVhaWtvMCJ9.xH-3a-x9qOF11YWF08rM6Q' })