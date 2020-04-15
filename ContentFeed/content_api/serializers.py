from rest_framework import serializers
from content_api.models import User, Item

# THIS SERIALIZES THE ITEM MODEL
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'Image', 'FirstName', 'LastName', 'Email', 'State', 'City', 'ZipCode', 'Password', 'created_at', 'updated_at', 'objects'

# THIS SERIALIZES THE ITEM MODEL
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = 'id', 'title', 'description', 'image'

