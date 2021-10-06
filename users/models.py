from django.db import models
from sorl.thumbnail import get_thumbnail

# Create your models here.

class UserModel(models.Model):
    questionsAsked = models.IntegerField(default=0)
    answersGiven = models.IntegerField(default=0)
    profilePic =  models.ImageField(upload_to='...')

    def __str__(self):
        return "\n".join([f"profilePic:{profilePic}", f"questionsAsked:{questionsAsked}", f"answersGiven:{answersGiven}"])
    
    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.profilePic, '300x300', quality=99, format='JPEG')
        super(UserModel, self).save(*args, **kwargs)
