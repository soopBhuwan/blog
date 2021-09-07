from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,'Draft'), (1,'Publish'),
)
class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length= 200,unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(timezone.now())
    subtitle = models.TextField(max_length = 150,default = "")
    content = models.TextField(max_length = 500)
    created_on = models.DateTimeField(timezone.now())
    status = models.IntegerField( choices = STATUS,default = 0)
    #anything that is not a field is stored in the Meta class
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
