from django.urls import include, path
from . import views

# urlpatterns = [
#     path('',views.page),
# ]


# urlpatterns = [
#     path('signup/',views.signup),
# ]

# urlpatterns = [
#     path('',views.login),
# ]

# urlpatterns = [
#     path('',views.forgotpsw),
# ]

# urlpatterns = [
#     path('',views.success),
# ]

urlpatterns = [
    path('',views.web),
    path('aboutpage/',views.aboutpage),
]