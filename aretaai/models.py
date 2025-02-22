from django.db import models

class Query(models.Model):
    query_text = models.CharField(max_length=200)
    query_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    def __str__(self):
        return self.query_text  

    class Meta:
        app_label = 'aretaai'

    def __str__(self):
        return self.text
