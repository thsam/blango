from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from rest_framework import permissions
from blog.api.serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author