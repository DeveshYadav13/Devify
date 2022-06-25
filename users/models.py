from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=2000,blank=True,null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to = 'profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE , null=True, blank=True )
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

def createProfile(sender, instance, created, **kwargs):
    print('Profile Saved!')
    if created: 
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
    
def deleteUser(sender,instance, **kwargs):
    print('DELETING USER....')

post_save.connect(createProfile,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)