from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, Profile,Product, ProductPost
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden


# Create your views here.
def home(request):
    productposts = Product.objects.all().order_by("-created_at")
    categories = Categories.objects.all()

    if request.user.is_authenticated:
        form = ProductForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                productpost = form.save(commit=False)
                productpost.user = request.user
                productpost.save()
                messages.success(request, ("Your Product Has Been Posted!"))
                return redirect('home')
        return render(request, 'home.html', {"productposts": productposts, "form": form, "categories": categories})
    else:
        return render(request, 'home.html', {"productposts": productposts, "categories": categories})

def about_us(request):
    return render(request,"about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('home')

    
def admin_session(request):
    return render(request, 'admin.html', {})

def profile(request, pk):
    if request.user.is_authenticated:
        profile,created = Profile.objects.get_or_create(user=request.user)
        products = Product.objects.filter(owner = request.user).order_by("-created_at")
        return render(request, "profile.html", {"profile":profile, "products":products})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home') 

def product_details(request, pk):
    product = get_object_or_404(Product, id=pk)

    # Handling POST request for updates or deletes if needed here
    if request.method == 'POST':
        if request.user != product.owner:
            # If not the owner, deny the ability to update or delete
            return HttpResponseForbidden("You are not authorized to edit or delete this product.")

        if 'update' in request.POST:
            # Assuming you have some form or method to handle updates
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect('some-view-name')  # Redirect after POST
        elif 'delete' in request.POST:
            product.delete()
            return redirect('some-view-name')  # Redirect to another view after delete

    # Display details page for GET requests
    return render(request, 'product_details.html', {'product': product})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        
        
       # user_form = SignUpForm(request.POST or None,request.FILES or None,instance = current_user)
        profile_form = ProfileForm(request.POST or None,request.FILES or None,instance = profile_user)
        if profile_form.is_valid():
            profile_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("Your Profile has been updated")) 
            return redirect( 'home')
        return render(request, 'update_user.html', {'profile_form':profile_form })

    else:
        messages.success(request, ("You must be logged in to view this page")) 
        return redirect( 'home')
    
@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product details updated successfully.")
            return redirect('home')
    else:
        product_form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'product_form': product_form})
    

def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product = product_form.save(commit=False)
                product.owner = request.user
                product.save()
                return redirect('home')
            else:
                error_message = "There was an error with your form"
                product_form = ProductForm(request.POST, request.FILES)
                product_postage = ProductPost.objects.all().order_by("-created_at")
                return render(request, 'add_product.html', {"product_postage": product_postage, "product_form": product_form, "error_message": error_message})
        else:
            product_form = ProductForm()
            product_postage = ProductPost.objects.all().order_by("-created_at")
            return render(request, 'add_product.html', {"product_postage": product_postage, "product_form": product_form})
    else:
        product_postage = ProductPost.objects.all().order_by("-created_at")
        return render(request, 'add_product.html', {"product_postage": product_postage})
        
def search_products(request):
    
    if request.method == "POST":
        searched = request.POST.get('searched','')
        products = Product.objects.filter(
            Q(name__contains=searched)| 
            Q(product_description__contains=searched) |  
            Q(product_price__contains=searched) 
            )
            
        return render(request, 'searched.html', {'searched': searched, 'products': products})
    else:
            return render(request, 'searched.html', {'searched': ""})

def delete_product(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            product = Product.objects.get(id=pk)
            product.delete()
            messages.success(request, "Product deleted successfully!")
            return redirect('home')
        else:
            return render(request, 'product_details.html', {'product_id': pk})
    else:
        messages.info(request, "You must be logged in!")
        return redirect('home')

def page_not_found(request, slug):
    return render(request, 'page_not_found.html',{'slug':slug})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please check the details and try again.")
    else:
        form = SignUpForm()
    return render(request, 'register_user.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Categories, Product

# This view should show all categories
def list_categories(request):
    categories = Categories.objects.all().order_by('name')
    return render(request, 'category_list.html', {'categories': categories})

# This view should show products for a specific category
def category_products(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})


