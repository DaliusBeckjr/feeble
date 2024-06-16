from django.db import models

import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        return errors
    
    def login_validator(self, postData):
        errors = {}
        return errors