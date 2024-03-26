from django.db import models
from datetime import datetime



class Room(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    
    def __str__(self):
        return self.room + ":" + self.name + ":" + str(self.date)
    
    
    
    
from django.db import models
from django.contrib.auth.models import User



class ChatMessages(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return ChatMessages.objects.order_by('-timestamp').all()[:10][::-1]
    