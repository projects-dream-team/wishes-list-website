from django.shortcuts import render
from products.models import Product
from core.models import TeamMember


def home(request):
    products = Product.objects.shop_products()[:8]
    team = TeamMember.objects.active()[:3]
    return render(request, 'home/home.html',{'products':products, 'team':team})
