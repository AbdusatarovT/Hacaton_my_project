
from user_profile.models import UserProfile, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import IsOwnerOrReadOnly
from . serializers import CommentSerializer, ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fielsd = ['gender']
    ordering_fields = ['studies_at', 'lives_in', 'works_at']
    search_fields = ['nik_name']
                         

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)