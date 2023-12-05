from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('app/', view=views.showform, name='app'),
    path('prediction/', view=views.getform, name='getform'),
]
