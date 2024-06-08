from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .models import *

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})

def about(request): 
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def add_to_cart(request):
    pk = request.GET.get('pk')
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.create(product = product,qty = 1)
    return redirect('/')

def services(request):
    cart = Cart.objects.all()
    return render(request, 'services.html',{'cart':cart})
    #return HttpResponse("this is services page")

def addtocart(request):
        return render(request, 'index.html')

def order(request):
    return render(request, "order.html")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

def redirect_to_social_media(request, platform):
    # Dictionary to map platform names to their corresponding URLs
    social_media_urls = {
        'facebook': 'https://www.facebook.com/your_facebook_page',
        'twitter': 'https://twitter.com/your_twitter_handle',
        'instagram': 'https://www.instagram.com/your_instagram_account',
        # Add more social media platforms and their URLs as needed
    }

    # Check if the requested platform is valid
    if platform in social_media_urls:
        # Redirect to the URL of the requested social media platform
        return redirect(social_media_urls[platform])
    else:
        # Redirect to a default page or return an error message
        return redirect('default_page_url')
