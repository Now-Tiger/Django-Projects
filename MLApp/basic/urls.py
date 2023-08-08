from django.urls import path
from . import views

urlpatterns = [
    # path('', view=views.root, name="Root"),
    path('home', view=views.welcome, name="Welcome"),
    path('user/', view=views.user, name="User"),
]
