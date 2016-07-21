from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   return render_to_response('adverts/home.html',
                             {})