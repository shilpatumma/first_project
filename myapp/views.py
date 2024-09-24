from django.shortcuts import render, get_object_or_404

# from.models import Student
# def std(request):
#     student = Student.objects.all()
#     return render(request, "std.html", {'studen': student})

# def std_list(request):
#     student = Student.objects.all()
#     return render(request, "std_list.html", {'student': student})




# def page(request):
#     return render(request, "page.html")



# def login(request):
#     return render(request, "login.html")

# def signup(request):
#     return render(request, "signup.html")

# def forgotpsw(request):
#     return render(request, "forgotpsw.html")

# def success(request):
#     return render(request, "success.html")



# def web(request):
#     return render(request, "web.html")

# def about_webpage(request):
#     return render(request, "about_webpage.html")



# posts = [
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'content': 'War and Peace',
#         'published_at': '1867'
#     },

#     {
#         'title': 'Time Machine',
#         'author': 'H.G Wells',
#         'content': 'Time Machine',
#         'published_at': '1895'
#     }
# ]

# def base(request):
#     return render(request, "blog/base.html")

# def home_template(request):
#     context = {
#         'posts' : posts,
#         'title' : Home,
#     }
#     return render(request, "blog/home_template.html", context)

# def about_template(request):
#     return render(request, "blog/about_template.html")



# from .models import Post

# def post_home(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_home.html', {'posts': posts})

# def post_about(request, id):
#     post = get_object_or_404(Post, id = id)
#     return render(request, 'blog/post_about.html', {'post': post})
    
# def layout(request):
    # return render(request, "blog/layout.html")


def form(request):
    return render(request, "blog/form.html")