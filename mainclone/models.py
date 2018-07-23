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

    def follow(self,profile):
        if self.following.filter(followee=profile).count() == 0:
            Follows(followee=profile, follower=self).save()

    def like(self,photo):
        if self.likes.filter(photo=photo).count() == 0:
            Likes(photo=photo,user=self).save()

    def comment(self,photo,text):
        Comments(text=text,photo=photo, user=self).save()


class Post(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(Profile, related_name='posts')


class Comments(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(Profile, related_name='comments')


class Likes(models.Model):
    user = models.ForeignKey(Profile, related_name='likes')
    photo = models.ForeignKey(Profile, related_name='likes')


class Follows(models.Model):
    follower = models.ForeignKey(Profile, related_name='following')
    followee = models.ForeignKey(Profile, related_name='followers')