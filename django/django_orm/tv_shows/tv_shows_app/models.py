from django.db import models
from datetime import datetime
import datetime as dt

# Create your models here.

class ShowManager(models.Manager):
    def validator(self, requestPOST):
        errors = {}
        for k in requestPOST:
            if k != "desc":
                if requestPOST[k] == '':
                    errors['fields'] = "All required fields must be filled out"
                    return errors
        title = Show.objects.filter(title=requestPOST['title'])
        if len(title) > 0:
            errors['duplicate'] = "This show is already in the database"
        if len(requestPOST['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(requestPOST['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        x = requestPOST['release_date']
        y = datetime.strptime(x, '%Y-%m-%d').date()
        if y > dt.date.today():
            errors['release_date'] = "Release date must be in the past"
        if len(requestPOST['desc']) > 0 and len(requestPOST['desc']) < 10:
            errors['desc'] = "Description must be at least 10 characters"
        return errors
    
    def edit_validator(self, requestPOST):
        errors = {}
        submission = []
        for k in requestPOST:
            if requestPOST[k] != '':
                submission.append(requestPOST[k])
                if k == "title":
                    title = Show.objects.filter(title=requestPOST[k])
                    if len(title) > 0:
                        errors['duplicate'] = "This show is already in the database"
                    if len(requestPOST[k]) < 2:
                        errors['title'] = "Title must be at least 2 characters"
                if k == "network" and len(requestPOST[k]) < 3:
                    errors['network'] = "Network must be at least 3 characters"
                if k == "release_date":
                    x = requestPOST['release_date']
                    y = datetime.strptime(x, '%Y-%m-%d').date()
                    if y > dt.date.today():
                        errors['release_date'] = "Release date must be in the past"
                if k == "desc" and len(requestPOST[k]) < 10:
                    errors['desc'] = "Description must be at least 10 characters"
        if len(submission) < 3:
            errors['empty'] = "At least one field must be updated to update database"
        print(submission)
        print(len(submission))
        print(errors)
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()