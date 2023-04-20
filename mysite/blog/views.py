from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Post

# Create your views here.


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.published.all()
    return render(
        request, 'blog/post/list.html', {'post': posts}
    )


def post_detail(request: HttpRequest, year: int, month: int, day: int, post: str) -> HttpResponse:
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        published__year=year,
        published__month=month,
        published__day=day,
    )
    return render(request, 'blog/post/details.html', {'post': post})
