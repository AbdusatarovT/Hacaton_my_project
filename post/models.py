
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Post(models.Model):
    '''Модель поста'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=4000)
    post_image = models.ImageField(upload_to="post_image",null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content



class Like(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='Владелиц лайка')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name='пост')
    like = models.BooleanField('Лайк', default=False)

    def __str__(self):
        return f'{self.post} {self.like}'