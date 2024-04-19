from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
