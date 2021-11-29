from django import db
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='batman.png')
    
    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'
    
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
        
        
class Post (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'posts')
    timestamp = models.DateTimeField(default= timezone.now) 
    content = models.TextField()
    
    class Meta:
        ordering = ['-timestamp']   
    
    def __str__(self) -> str:
        return f'{self.user.username}: {self.content}'    

class Relationship(models.Model):
    
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relationships')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_to')
    
    def str(self) -> str:
        return f'{self.from_user.username} follows {self.to_user.username}'
    
    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user',]),
        ]
      

