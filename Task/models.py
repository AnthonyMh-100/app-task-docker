from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id')
    title = models.CharField(max_length=20,verbose_name='Titulo')
    description = models.TextField(verbose_name='Description')
    customer = models.CharField(max_length=30,verbose_name='Cliente')
    date_from = models.DateField(verbose_name='Fecha Inicial')
    date_to = models.DateField(verbose_name='Fecha Final')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    state = models.CharField(max_length=20, choices=(
        ('backlog', 'Backlog'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ), default='backlog',verbose_name='Estado')
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return self.title
    