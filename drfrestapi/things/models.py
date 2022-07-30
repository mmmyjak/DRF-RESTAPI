from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Thing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='things')
    name = models.CharField(max_length=100)
    importance = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='things', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['done', 'deadline']
    
    def __str__(self):
        return self.name

    def category_name(self):
        return self.category.name
