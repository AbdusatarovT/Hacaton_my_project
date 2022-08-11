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
        # representation['favorite'] = instance.favorits.filter(favorit=True)
        
        rating_res = 0
        for rating in instance.ratings.all():
            rating_res += int(rating.rating)
        try:
            representation['ratings'] = rating_res / instance.ratings.all().count()
        except ZeroDivisionError:
            pass
        return representation



class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)