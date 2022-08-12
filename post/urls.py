from rest_framework.routers import DefaultRouter
from post.views import PostViewSet, ContactView



router = DefaultRouter()

router.register('posts',PostViewSet)
router.register('', ContactView)

urlpatterns = []
urlpatterns.extend(router.urls)