from django.db import models

class Contact(models.Model):
        name = models.CharField(max_length=40)
        address = models.CharField(max_length=100)
        phone = models.CharField(max_length=50)
        email = models.CharField(max_length=60)
        contact_type = models.CharField(max_length=20)

        def __str__(self):
            return self.name

