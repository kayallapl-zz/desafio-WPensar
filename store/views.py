from django.shortcuts import render
from store.models import Product, History

def index(request):
    return render(request, "store/index.html")

def register(request):
    return render(request, "store/register.html")

def search(request):
    return render(request, "store/search.html")

def show_products_list(request):
    context = {}
    context["products"] = Product.objects.all()
    return render(request, "store/products.html", context)

def addproduct(request):
    product_name = request.POST.get("name")
    product_price = request.POST.get("price")
    new_product = Product(label=product_name, price=float(product_price))
    new_product.save()

    context = {}
    context["products"] = Product.objects.all()
    return render(request, "store/products.html", context)

def searchresult(request):
    product_name = request.POST.get("name")
    count = 0
    sum = 0
    context = {}
    context["product_name"] = product_name
    context["products"] = Product.objects.all()
    for product in context["products"]:
        if product.label == product_name:
            sum+=product.price
            count+=1
    if count>0:
        context["media"] = sum/count
    else:
        context["media"] = "Nenhum item cadastrado"
    return render(request, "store/searchresult.html", context)