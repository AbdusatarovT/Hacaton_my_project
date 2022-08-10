from . models import Post
from rest_framework import serializers
from user_profile.serializers import CommentSerializer
# from votes.serializers import VoteSerializer


class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    # votes=VoteSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = '__all__'