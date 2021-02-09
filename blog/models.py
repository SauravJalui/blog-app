from django.db import models

class Post(models.Model):
    '''This contains the post details required to be filled while creating the post using the admin panel'''
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        )
    body = models.TextField()

    def __str__(self):
        return self.title
