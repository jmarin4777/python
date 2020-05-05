from django.db import models
import re
from django.utils import timezone

# Create your models here.
class UserManager(models.Manager):
    def validator(self, requestPOST):
        errors = {}
        for k in requestPOST:
            if requestPOST[k] == '':
                errors['fields'] = "All fields must be filled out"
                return errors
        email_in_db = User.objects.filter(email=requestPOST['email'])
        if len(email_in_db) > 0:
            errors['duplicate'] = "Email address provided is already associated with an account"
            return errors
        if len(requestPOST['first_name']) < 2 or len(requestPOST['last_name']) < 2:
            errors['name'] = "First name and last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors['email'] = "Invalid email address"
        if len(requestPOST['pw']) < 8:
            errors['pw_length'] = "Password must be at least 8 characters"
        if requestPOST['pw'] != requestPOST['cf_pw']:
            errors['pw_match'] = "Passwords must match"
        return errors
    def editValidator(self, requestPOST):
        errors = {}
        for k in requestPOST:
            if requestPOST[k] == '':
                errors['fields'] = "All fields must be filled out"
                return errors
        email_in_db = User.objects.filter(email=requestPOST['email'])
        if len(email_in_db) > 0:
            errors['duplicate'] = "Email address provided is already associated with an account"
            return errors
        if len(requestPOST['first_name']) < 2 or len(requestPOST['last_name']) < 2:
            errors['name'] = "First name and last name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors['email'] = "Invalid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def validator(self, requestPOST):
        errors = {}
        for k in requestPOST:
            if requestPOST[k] == '':
                errors['fields'] = "All fields must be filled out"
                return errors
        if len(requestPOST['author']) < 4:
            errors['author'] = "Author name must be more than 3 characters"
        if len(requestPOST['quote']) < 11:
            errors['quote'] = "Quote must be more than 10 characters"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    user = models.ForeignKey(User, related_name="quotes", on_delete=models.CASCADE)
    users_who_liked= models.ManyToManyField(User, related_name="quotes_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()