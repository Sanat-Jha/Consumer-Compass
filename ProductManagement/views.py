from django.shortcuts import redirect, render

from ProductManagement.models import Category, Product
from ReviewManagement.models import Review
from UserManagement.models import Consumer

# Create your views here.
def product(request):
    product = Product.objects.get(title=request.POST.get("product_title"))
    ccreviews = Review.objects.filter(product=product)
    if len(Review.objects.filter(product=product,consumer=Consumer.objects.get(username=request.user.username)))==0:
        return render(request, 'product.html',{'product':product,'ccreviews':ccreviews,'username':request.user.username,"writereview":True})
    return render(request, 'product.html',{'product':product,'ccreviews':ccreviews,'username':request.user.username,"writereview":False})


def addproduct(request):
    if request.method == 'POST':
        product = Product(title=request.POST.get("title"),category=Category.objects.get(name=request.POST.get("category")),ccscore=0,amazonreviews=[],image=request.FILES['image'],flipkartreviews=[],online_rating=0,price=request.POST.get("price"))
        product.save()
        return  render(request, 'addproduct.html',{"redirect":True,"product_title":product.title})
    return render(request, 'addproduct.html',{'categories':Category.objects.all(),'redirect':False})