from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect, render

from ProductManagement.models import Product
from ReviewManagement.models import Review
from UserManagement.models import Consumer

# Create your views here.
def writereview(request,producttitle):
    product = Product.objects.get(title=producttitle)
    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        review = request.POST.get("review")
        if len(Review.objects.filter(product=product,consumer=Consumer.objects.get(username=request.user.username))) == 0:
            review = Review(product=product, content=review,consumer=Consumer.objects.get(username=request.user.username))
            review.save()
            l = len(Review.objects.filter(product=product))
            product.ccscore = (product.ccscore*(l-1) + rating)/l
            product.save()

        return render(request, 'writereview.html',{'product':product, 'redirect':True})
    return render(request, 'writereview.html',{'product':product, 'redirect':False})


# @csrf_exempt
def editreview(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        product_title = data.get('product')
        new_content = data.get('content')

        # Find the review by username and product
        try:
            review = Review.objects.get(consumer__username=username, product__title=product_title)
            review.content = new_content
            review.save()

            # Return success response
            return JsonResponse({'success': True,'content':new_content,'username':username})

        except Review.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Review not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

