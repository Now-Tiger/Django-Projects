from django.urls import path
from .views import UserListCreate, UserRetriveUpdateDelete

urlpatterns = [
    path('users', UserListCreate.as_view(), name='Create-User-List'),
    path('users/<int:pk>', UserRetriveUpdateDelete.as_view(), name='user-Details')
]
