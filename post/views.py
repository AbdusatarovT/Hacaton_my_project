from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets



class PostViewSet(viewsets.ModelViewSet):

    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)