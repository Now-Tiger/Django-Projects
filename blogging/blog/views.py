from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    """ Retrives all the posts with the published status """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'page':page,
         'posts': posts}
    )


class PostListView(ListView):
    """ classed based view for above method """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(
        request: HttpRequest, year: int, month: int, day: int, post: str
        ) -> HttpResponse:
    """ This view takes the year, month, day, and post
        arguments to retrieve a published post with the 
        given slug and date """
    post = get_object_or_404(
        Post, 
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )