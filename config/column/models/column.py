from django.db import models
from user.models.user import User
import uuid

class Column(models.Model):
    # column
    column_id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4)
    title = models.CharField(max_length=45, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    prefer = models.IntegerField(default=0)
    category = models.CharField(max_length=10)

    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)

    # series
    # series_series_id = models.IntegerField()
    # series_user_id = models.IntegerField()

    class Meta:
        db_table = 'column'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class ColumnPrefer(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='preferer')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Prefer: {self.user.userName}"