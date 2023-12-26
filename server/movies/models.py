from django.db import models

from movies.managers import MovieManager
from user.models import *




class Movie(models.Model):

    title = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    description = models.TextField()
    # one to many
    owner = models.ForeignKey(User, related_name='movies', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = MovieManager()


    def __str__(self):
        return f"""Movie Object():
                    title: {self.title}
                    Release Date: {self.release_date}
                    Duration: {self.duration}
                    Description: {self.description}
                    owner: {self.owner}"""