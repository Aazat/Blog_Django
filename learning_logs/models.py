from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something special learned about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return the string representation of the model"""
        return f"{self.text[:50]}..."
# Create your models here.
