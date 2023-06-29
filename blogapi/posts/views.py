from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import isAutherOrReadOnly

# Create your views here.


class PostList(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (isAutherOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
