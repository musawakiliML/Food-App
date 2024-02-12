from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# from django.template import loader


# Create your views here.

def index(request):
   item_list = Item.objects.all()
   #template = loader.get_template('app/index.html')

   context = {
      "item_list":item_list
   }

   #return HttpResponse(template.render(context, request))
   return render(request, "app/index.html", context)

def detail(request, item_id):
   item = Item.objects.get(pk=item_id)
   
   context = {
      "item": item, 
   }

   return render(request, "app/detail.html", context)