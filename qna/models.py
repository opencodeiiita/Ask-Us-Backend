from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=42)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    no_of_answers = models.IntegerField(default=0)
    no_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return "\n".join([
            f"[{title}]: {date_posted}",
            f"{description}",
            f"answers: {no_of_answers}",
            f"upvotes: {no_of_upvotes}",
        ])