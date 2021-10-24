from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=42)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    no_of_answers = models.IntegerField(default=0)
    no_of_upvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'#{self.id}: ' + self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    answer_text = models.TextField()
    no_of_upvotes = models.IntegerField(default=0)
    no_of_downvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'QID {self.question.id}: ' + self.answer_text[:16] + '...'
