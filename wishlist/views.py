from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from wishlist.models import ItemWishlist

def show_wishlist(request):
    data_wishlist_item = ItemWishlist.objects.all()
    context = {
    'list_item': data_wishlist_item,
    'name': 'NicolasAnanda'
    }
    return render(request, "wishlist.html", context)
    
def show_xml(request):
    data = ItemWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemsWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request):
    data = ItemsWishlist.objects.filter(pk=id)
    // JSON Format
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    // XML Format
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Create your views here.
