from django.shortcuts import render
from store.models import Product, History

# Create your views here.
def buy_product(request):
    product_id = request.POST.get("productid")
    product = Product.objects.get(product_id=product_id)
    history = History(product_id=product_id, user=request.user, price=product.price)
    history.save()
    return render(request, "store/confirmbuy.html")

def home(request):
    return render(request, 'store/index.html')