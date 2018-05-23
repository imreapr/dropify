from django.shortcuts import render
from django.http import HttpResponse
import webapp.utils
import webapp.forms
# Create your views here.
def index(request):

    product_des = {
    'name' :  webapp.utils.name,
    'price' : webapp.utils.price,
    'orders' : webapp.utils.orders,
    'link' : webapp.utils.link,
    }

    context = {'product_des' : product_des}
    return render(request, 'webapp/product.html',context)
