from django.db import models
from django.db import models

class Query(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entity(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    text = models.TextField()
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.text
