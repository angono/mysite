from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


# Create your models here.
class PhotoModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to="users-images")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f"{self.author} - {self.title}"


    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk]) 





