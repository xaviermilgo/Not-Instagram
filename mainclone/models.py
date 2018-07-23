from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(default="Welcome Me!")

    @classmethod
    def usercheck(cls,user):
        if cls.objects.filter(user=user).count() == 0:
            print("has no profile!")
            cls(user=user).save()


class Post(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(Profile)