from django.db import models

# ONE Dungeon has MANY prisoners
# ONE prisoner has ONE Dungeon
# ONE to MANY relationship

# Create your models here.
class Dungeon(models.Model):
    name = models.CharField(max_length=255)
    num_people_inside = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Prisoner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    dungeon = models.ForeignKey(Dungeon, related_name="prisoners",
    on_delete=models.CASCADE)
    dislikes = models.ManyToManyField(Dungeon, related_name=
    "prisoner_dislikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)