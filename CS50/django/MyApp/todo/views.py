from django.shortcuts import render

# Create your views here.
def index(request):
    todo=["khana","kaaam","tatti"]
    return render(request,"todo/index.html",{
        "todo":todo

    })