from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.insert(0, './yolov5')
# Create your models here.

class post():
    title=models.CharField
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField
    
    
    
    def __str__(self):
        return self.title
    
    
    
    
