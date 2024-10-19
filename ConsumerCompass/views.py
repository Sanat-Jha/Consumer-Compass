


from django.shortcuts import render

from ProductManagement.models import Category
def welcomepage(request):
    cats = Category.objects.all()
    context  ={
        "cats":cats
    }
    if request.user.is_authenticated:
        context["username"] = request.user.username
    return render(request,"welcome.html",context)

