from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 225)
    description = models.CharField(max_length = 225)
    body = models.TextField(blank = True, null = True)
    date  = models.DateField(auto_now_add= True,)
    cover = models.ImageField(upload_to='blogs/', blank= True , null= True)
    #author

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.cover.url
        except:
            url = ''
        return url