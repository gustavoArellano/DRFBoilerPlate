from rest_framework import serializers
from content_api.models import User, Item
from django.contrib.auth.hashers import make_password
import bcrypt



# THIS SERIALIZES THE ITEM MODEL
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'Image', 'FirstName', 'LastName', 'Email', 'State', 'City', 'ZipCode', 'Password', 'created_at', 'updated_at'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            FirstName = validated_data['FirstName'],
            LastName = validated_data['LastName'],
            Email = validated_data['Email'],
            State = validated_data['State'],
            City = validated_data['City'],
            ZipCode = validated_data['ZipCode'],
            Password = make_password(validated_data['Password'])
        )
        user.save()
        return user

# THIS SERIALIZES THE ITEM MODEL
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = 'id', 'title', 'description', 'image'

