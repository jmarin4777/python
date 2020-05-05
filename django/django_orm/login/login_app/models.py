from django.db import models
import re
from datetime import datetime, timedelta
import datetime as dt

# Create your models here.
class UserManager(models.Manager):
    def validator(self, requestPOST):
        errors = {}
        email_in_db = User.objects.filter(email=requestPOST['email'])
        if len(email_in_db) > 0:
            errors['duplicate'] = "Email address provided is already associated with an account"
            return errors
        for k in requestPOST:
            if requestPOST[k] == '':
                errors['fields'] = "All fields must be filled out"
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
        x = requestPOST['birthday']
        y = datetime.strptime(x, '%Y-%m-%d').date()
        if y > dt.date.today():
            errors['birthday'] = "Birthday must be in the past"
        day, month = dt.date.today().day, dt.date.today().month
        years = timedelta(days=365.2425)
        age_13 = dt.date.today() - years*13
        date_to_check = f"{age_13.year}-{month}-{day}"
        date_to_check = datetime.strptime(date_to_check, '%Y-%m-%d').date()
        if y > date_to_check:
            errors['thirteen'] = "You must be at least 13 years old to enter"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255,null=True)
    birthday = models.DateField(null=True)
    objects = UserManager()