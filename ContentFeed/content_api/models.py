from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from time import strftime
from django import forms
import re
import bcrypt
from django.conf import settings
from rest_framework import serializers



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def first_name_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("FIRST NAME cannot be BLANK!")
    elif len(data) < 2:
        raise serializers.ValidationError("FIRST NAME must contain at least 2 letters MINIMUM!")
    elif not data.isalpha():
        raise serializers.ValidationError("FIRST NAME must contain letter's ONLY!")
    return data

def last_name_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("LAST NAME cannot be blank!")
    elif len(data) < 2:
        raise serializers.ValidationError("LAST NAME must contain at least 2 letters MINIMUM!") 
    elif not data.isalpha():
        raise serializers.ValidationError("LAST NAME must contain letter's ONLY")
    return data

def email_validator(data):
    if User.objects.filter(Email = data):
        raise serializers.ValidationError("An account has already been created with this EMAIL!")
    if EMAIL_REGEX.match(data) == None:
        raise serializers.ValidationError("Invalid EMAIL FORMAT! ")
    elif len(data) < 1:
        raise serializers.ValidationError("EMAIL cannot be BLANK!")

def state_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("You must select a STATE!")

def city_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("You must select a City!")

def zip_code_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("You must enter your ZIP CODE!")
    if len(data) != 5:
        raise serializers.ValidationError("You must enter a valid ZIP CODE!") 

def password_validator(data):
    if len(data) < 1:
        raise serializers.ValidationError("PASSWORD cannot be BLANK!")
    elif len(data) < 6:
        raise serializers.ValidationError("PASSWORD must be at least 6 characters MINIMUM!")


class UserManager(models.Manager):
    def RegValidation(self, postData):
        errors = {}

        # if postData['Password'] != postData['ConfirmPassword']:
        #     errors['ConfirmPassword'] = "PASSWORDS do not MATCH!"

        return errors

    def LoginValidation(self, postData):
        user = User.objects.filter(Email = postData['LoginEmail'])
        errors = {}
        if not user:
            errors['Email'] = "Invalid EMAIL or PASSWORD!"

        HashPW = bcrypt.hashpw(postData['LoginPassword'].encode('utf-8'), bcrypt.gensalt())

        if user and not bcrypt.checkpw(postData['LoginPassword'].encode('utf-8'), HashPW):
            errors['Password'] = "Invalid EMAIL or PASSWORD!"

        return errors

    def UserUpdateValidations(self, postData): 
        errors = {}

        if len(postData['FirstName']) < 1:
            errors['FirstName'] = "FIRST NAME cannot be BLANK!"
        elif len(postData['FirstName']) < 2:
            errors['FirstName'] = "FIRST NAME must contain at least 2 letters MINIMUM!"
        elif not postData['FirstName'].isalpha():
            errors['FirstName'] = "FIRST NAME must contain letter's ONLY!"

        if len(postData['LastName']) < 1:
            errors['LastName'] = "LAST NAME cannot be blank!"
        elif len(postData['LastName']) < 2:
            errors['LastName'] = "LAST NAME must contain at least 2 letters MINIMUM!" 
        elif not postData['LastName'].isalpha():
            errors['LastName'] = "LAST NAME must contain letter's ONLY"

        if User.objects.filter(Email = postData['Email']):
            errors['EmailExists'] = "An account has already been created with this EMAIL!"
        if EMAIL_REGEX.match(postData['Email']) == None:
            errors['EmailFormat'] = "Invalid EMAIL FORMAT!"
        elif len(postData['Email']) < 1:
            errors['Email'] = "EMAIL cannot be BLANK!"

        if len(postData['State']) < 1:
            errors['State'] = "You must select a STATE!"

        if len(postData['City']) < 1:
            errors['City'] = "You must select a City!"

        if len(postData['ZipCode']) < 1:
            errors['ZipCode'] = "You must enter your ZIP CODE!"
        if len(postData['ZipCode']) != 5:
            errors['ZipCode'] = "You must enter a valid ZIP CODE!" 

        return errors

class User(models.Model): 
    Image = models.ImageField(default='/default/placeholder.png', upload_to='images', blank = True, null = True)
    FirstName = models.CharField(max_length = 20, validators=[first_name_validator]) 
    LastName = models.CharField(max_length = 20, validators=[last_name_validator])
    Email = models.EmailField(max_length = 255, validators=[email_validator])
    State = models.CharField(max_length = 2, validators=[state_validator])
    City = models.CharField(max_length = 20, validators=[city_validator])
    ZipCode = models.CharField(max_length = 5, validators=[zip_code_validator])
    Password = models.CharField(max_length = 255, validators=[password_validator])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')