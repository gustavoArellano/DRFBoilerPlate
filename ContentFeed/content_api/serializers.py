from rest_framework import serializers
from content_api.models import User, Item

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# def RegValidation(self, postData, firstname):
#     errors = {}

#     if len(postData['FirstName']) < 1:
#         raise serializers.ValidationError("FIRST NAME cannot be BLANK!")
#     elif len(postData['FirstName']) < 2:
#         serializers.ValidationError("FIRST NAME must contain at least 2 letters MINIMUM!")
#     elif not postData['FirstName'].isalpha():
#         serializers.ValidationError("FIRST NAME must contain letter's ONLY!")

#     return print(errors)

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

