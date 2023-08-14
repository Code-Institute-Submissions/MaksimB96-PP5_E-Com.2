from django.db import models


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class NewsLetter(models.Model):
    title = models.CharField(max_length=100, null=True)
    news_body = models.TextField(null=True)
    
    def __str__(self):
        return self.title
