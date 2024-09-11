from django.urls import include, path
from . import views

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


urlpatterns = [
    path('',views.home_template),
    path('about_template/',views.about_template),
    path('base/', views.base),
]