	# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Developer(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	bio = models.CharField(max_length=255)
	especiality = models.CharField(max_length=255)
	picture = models.ImageField(blank=True)
	email = models.EmailField()
	curriculum = models.FileField(blank=True, null=True)
	# curriculum = models.FileField(blank=True, null=True ,upload_to=generate_path)	
	def __str__(self):
		return self.name


class Templates(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	developer = models.ForeignKey(Developer, null=True, blank=True, on_delete=models.CASCADE)
	url = models.CharField(max_length=255)
	picture = models.ImageField(blank=True)
	dtex = models.CharField(max_length=255)
	dimg = models.CharField(max_length=255)
	def __str__(self):
		return self.name