from .serializers import PostSerializer
from .models import Post, Like
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from user_profile.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, post_id=pk)
            like_object.like = not like_object.like
            like_object.save()
            status = 'liked'

            if like_object.like:
                return Response({'status': status})
            status = 'unliked'
            return Response({'status': status})
        except Exception as e:
            print(e)
            return Response('Нет такого поста!')