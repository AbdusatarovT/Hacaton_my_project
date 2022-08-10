from rest_framework.routers import DefaultRouter
from post.views import PostViewSet



router = DefaultRouter()

router.register('posts',PostViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)