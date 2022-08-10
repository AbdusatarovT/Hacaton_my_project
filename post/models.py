
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=4000)
    post_image = models.ImageField(upload_to="post_image",null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content