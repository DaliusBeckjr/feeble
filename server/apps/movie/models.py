from django.db import models
from apps.movie.managers import MovieManager
from apps.user.models import User

class Movie(models.Model):
    title = models.CharField(max_length=45)
    duration = models.IntegerField()
    description = models.TextField()
    released_date = models.DateField()
    rated = models.IntegerField()
    
    created_by = models.ForeignKey(User, related_name = 'movies', on_delete = models.CASCADE, null = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# now when we print our object to the terminal, we
# will get our information in this structure
#  instead
    def __str__(self):
        return f"""movie object():
                    Title: {self.title},
                    duration: {self.duration},
                    description: {self.description},
                    released date: {self.released_date},
                    rated: {self.rated},
                    created by: {self.created_by}
                """