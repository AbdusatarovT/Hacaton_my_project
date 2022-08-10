from . models import Post
from rest_framework import serializers
from user_profile.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
   
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation