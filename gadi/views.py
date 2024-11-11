from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html') 

def boys(request):
    return render(request, 'cart.html') 

def boys_product(request):
    return render(request, 'boys_product.html') 


def checkout_cart_view(request):
    return render(request, 'cart.html')

def register_account_view(request):
    return render(request, 'register_account.html')

def login_account_view(request):
    return render(request, 'login_account.html')

def buy_now_views(request):
    return render(request, 'buy_now.html')