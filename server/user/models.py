from django.db import models


from user.managers import UserManager


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    def __str__(self):
        return f""" User object():
                    First Name: {self.first_name}
                    Last Name: {self.last_name}
                    Email: {self.email}"""
