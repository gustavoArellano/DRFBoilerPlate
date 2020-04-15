from rest_framework import serializers
from content_api.models import Item

# THIS SERIALIZES THE MODEL
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = 'id', 'title', 'description'