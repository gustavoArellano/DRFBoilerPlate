from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

# IMPORT VIEWS FROM "CONTENT_API" FOLDER
from content_api.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url('admin/', admin.site.urls),
]
