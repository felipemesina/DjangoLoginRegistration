# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors=[]
        if len(self.filter(email = post_data['email'])) > 0:
            user = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password are incorrect')
        else:
            errors.append('email/password are incorrect')
        if errors:
            return errors
        return user
    
    def validate_registration(self, post_data):
        errors = []
        if len(post_data['first_name']) < 2:
            errors.append("First name must be at least 2 characters")
        if len(post_data['last_name']) < 2:
            errors.append("Last name must be at least 2 characters")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('Name fields must contain letters only')
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append('Invalid email format')
        if len(post_data['password']) < 8:
            errors.append('Password length must be at least 8 characters')
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email is already taken")
        if post_data['password'] != post_data['password_confirm']:
            errors.append("Passwords do not match")
        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                        first_name = post_data['first_name'],
                        last_name = post_data['last_name'],
                        email = post_data['email'],
                        password = hashed
            )
            return new_user
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email
