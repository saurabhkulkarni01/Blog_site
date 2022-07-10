from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})    

class sample_no(models.Model):
    Sample_No=models.CharField(max_length=32)
    Model_Code=models.CharField(max_length=32)
    Sub_Category=models.CharField(max_length=64)
    Curr_Location=models.CharField(max_length=64)
    Curr_Assignee=models.CharField(max_length=32)
    STPI=models.CharField(max_length=32)

    def _str_(self) -> str:
        return self.Sample_No
