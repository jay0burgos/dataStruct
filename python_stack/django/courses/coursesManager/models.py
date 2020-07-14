from django.db import models

# Create your models here.
class description(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class course(models.Model):
    name = models.CharField(max_length = 50)                                    #allows for deletion after course is deleted
    descrip = models.OneToOneField(description, related_name="courses", null = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

