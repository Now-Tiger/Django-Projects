from django.urls import path
from . import views

urlpatterns = [
    # path("books/", view=views.books),
    # api/books/1
    path(
        "books/",
        view=views.BookView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "books/<int:pk>",
        view=views.BookView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
]
