from django.urls import include, path
from . import views
from django.contrib import admin


# urlpatterns = [
#     path('',views.page),
# ]




# urlpatterns = [
#     path('',views.login),
#     path('signup/',views.signup),
#     path('forgotpsw/', views.forgotpsw),
#     path('success/', views.success),
# ]



# urlpatterns = [
#     path('',views.web),
#     path('about_webpage/',views.about_webpage),
# ]


# urlpatterns = [
#     path('',views.home_template),
#     path('about_template/',views.about_template),
#     path('base/', views.base),
# ]



# urlpatterns = [
#     path('',views.std),
#     path('std_list/', views.std_list ,name='page'),
# ]


# app_name = 'myapp'

# urlpatterns = [
#     path('', views.post_home, name = "list"),
#     path('layout/', views.layout),
#     path('post/<int:id>/', views.post_about, name= "page"),
# ]



urlpatterns = [
    path('', views.form),
]