from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_views(request):
    
    return HttpResponse('Welcome to CN334 Juzi Viwe!')

def home_page(request):
    return render(request, 'home-page.html')

def category_page(request):
    return render(request, 'category-page.html')

def checkout_page(request):
    return render(request, 'checkout-page.html')

def contact_page(request):
    return render(request, 'contact-page.html')

def product_page(request):
    return render(request, 'product-page.html')