from django.shortcuts import render,get_object_or_404
from .models import Product,Cart
from .models import UserProfile
# Create your views here.
from django.contrib.auth.decorators import login_required

def home_view(request):
    category = request.GET.get('category', None)
    
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'home.html',{'products': products} )


def boys(request):
    return render(request, 'cart.html') 

def boys_product(request):
    return render(request, 'boys_product.html') 
def category_products(request, category_name):
    """
    View to display products based on category (e.g., 'boys', 'ladies', 'unisex').
    """
    carts = Cart.objects.prefetch_related('products')
    # Fetch products based on category
    products = Product.objects.filter(category__iexact=category_name)  # Case-insensitive filter

    # Render the template with the products in the selected category
    return render(request, 'boys_product.html', {'products': products, 'category_name': category_name,'carts': carts})


def checkout_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'cart.html', {'product': product})



@login_required
def buy_now_views(request,product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'buy_now.html',{'product': product})





from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

def register_account_view(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register_account')

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register_account')

        # Create user
        user = User.objects.create_user(
            username=email,  # Using email as the username
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
            
        )
        # UserProfile.objects.create(user=user, phone=phone)

        # user.UserProfile.save()
        # Authenticate and log in the user
        login(request, user)

        # Retrieve full name using `get_full_name()`
        full_name = user.get_full_name()
        messages.success(request, f"Welcome, {full_name}!")

        # Redirect to a success page or dashboard
        return redirect('home')

    return render(request, 'register_account.html')


def login_account_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Get user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email is incorrect!')
            return redirect('login_account')

        # Authenticate using the username (as authenticate expects the username)
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login_account')

    return render(request, 'login_account.html')


