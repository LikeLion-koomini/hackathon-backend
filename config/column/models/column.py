from django.db import models
from user.models import CustomUser

class Column(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    prefer = models.IntegerField()
    series_series_id = models.IntegerField()
    series_user_id = models.IntegerField()
    category = models.CharField(max_length=10)

    class Meta:
        db_table = 'column'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class ColumnPrefer(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='prefer')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Prefer: {self.user.username}"