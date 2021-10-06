from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail

# Create your models here.

class UserModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    questionsAsked = models.IntegerField(default=0)
    answersGiven = models.IntegerField(default=0)
    profilePic =  models.ImageField(upload_to='profile_pics', default='default.png')

    def __str__(self):
        return "\n".join([f"profilePic:{self.profilePic}", f"questionsAsked:{self.questionsAsked}", f"answersGiven:{self.answersGiven}"])
    
    def save(self, *args, **kwargs):
        if self.profilePic:
            self.profilePic = get_thumbnail(self.profilePic, '300x300', quality=99, format='JPEG').url
        super(UserModel, self).save(*args, **kwargs)
