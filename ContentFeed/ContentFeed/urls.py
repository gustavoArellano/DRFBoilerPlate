from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

# IMPORT VIEWS FROM "CONTENT_API" FOLDER
from content_api.views import UserViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'item', ItemViewSet, basename='item')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
