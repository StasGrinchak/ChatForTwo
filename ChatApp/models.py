from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):

    """Model for user communication thread"""

    participants = models.ManyToManyField(User, related_name="tread_user",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.created)
    

class Message(models.Model):

    """Model for user messages tied to a thread"""

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_for_message')
    text = models.TextField(default='')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='message')
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.sender.username)
