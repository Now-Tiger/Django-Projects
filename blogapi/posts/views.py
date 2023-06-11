from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
