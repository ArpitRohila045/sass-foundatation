from django.http import HttpResponse as Http
from django.shortcuts import render
from visits.models import PageVisits
import pathlib


DIR = pathlib.Path(__file__).resolve().parent

my_context = {
    "name" : "My Saas app"
}
    
def home_view(request):
    PageVisits.objects.create(page_name=request.path)
    qs = PageVisits.objects.filter(page_name=request.path)

    my_context = {
        "name" : "My Saas app",
        "page_visits" : qs.count(),
        "total_visits" : PageVisits.objects.all().count()
    }

    return render(request, "base.html", context=my_context)

def new_home_view(request):
    PageVisits.objects.create(page_name=request.path)
    qs = PageVisits.objects.filter(page_name=request.path)

    my_context = {
        "name" : "My Saas app",
        "page_visits" : qs.count(),
        "total_visits" : PageVisits.objects.all().count()
    }

    return render(request, "home.html", context=my_context)