from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

class game(models.Model):
    name = models.CharField(max_length=100)
    download = models.IntegerField()
    Genre = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    download_link = models.URLField(default="")
    date_release = models.DateTimeField(default=timezone.now)
    game_img = models.ImageField(upload_to= 'game_img/' , default='default.jpg')
    
    def __str__(self):
        return self.name



class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name = models.ForeignKey(game, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
