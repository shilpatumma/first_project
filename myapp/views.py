from django.shortcuts import render

# def page(request):
#     return render(request, "page.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

# def forgotpsw(request):
#     return render(request, "forgotpsw.html")

# def success(request):
#     return render(request, "success.html")


# def menu(request):
#     return render(request, "menu.html")
