from django.db import models
from user.models.user import User
import uuid
from datetime import datetime

class Series(models.Model):
    series_id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4)
    title = models.CharField(null=False, max_length=100)
    content = models.CharField(null=False, max_length=500)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    writerName = models.CharField(null=True, max_length=100, default=None)
    columnCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)