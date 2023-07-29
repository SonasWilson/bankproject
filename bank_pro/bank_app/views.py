from django.shortcuts import render
from . models import service
# Create your views here.
def index(request):
     val = service.objects.all()
     return render(request,"index.html", {'result':val})

#