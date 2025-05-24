from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello/sample.html', {'name': 'World'})


def product_temp(request):
    return render(request, 'hello/product.html')

def about_us(request):
    return render(request, 'hello/about.html')
