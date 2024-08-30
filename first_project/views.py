# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello World!")

# def home(request):
#     return HttpResponse("This is my home")




from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")