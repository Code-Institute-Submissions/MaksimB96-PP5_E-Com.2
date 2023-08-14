from django.db import models

# Create your models here.
class ContactForm(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.full_name