from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField("message", max_length=255)
    read = models.BooleanField("read", default=False)
    created_at = models.DateTimeField("created_at", auto_now_add=True)

    ordering = "-created_at"
