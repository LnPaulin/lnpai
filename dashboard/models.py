from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4

from django_resized import ResizedImageField

import os



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    region = models.CharField(null=True, blank=True, max_length=50)
    country =  models.CharField(null=True, blank=True, max_length=50)
    postalCode = models.CharField(null=True, blank=True, max_length=50)
    profileImage = ResizedImageField(size=[200, 200], quality=90, upload_to='profile_images')
    



#Utitity variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_udated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.email) 


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localdate(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            #self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.email))
    
        self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.user.email))
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=500)
    keyword = models.CharField(null=True, blank=True, max_length=500)
    audience = models.CharField(null=True, blank=True, max_length=100)
    wordcount = models.CharField(null=True, blank=True, max_length=500)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Utitity variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_udated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.title, self.uniqueId) 

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localdate(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
    
        self.slug = slugify('{} {}'.format(self.user.title, self.uniqueId) )
        self.last_updated = timezone.localtime(timezone.now())
        super(Blog, self).save(*args, **kwargs)


class BlogSection(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    blog = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Utitity variables
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_udated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.title, self.uniqueId) 

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localdate(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
    
        self.slug = slugify('{} {}'.format(self.user.title, self.uniqueId) )
        self.last_updated = timezone.localtime(timezone.now())
        super(BlogSection, self).save(*args, **kwargs)
