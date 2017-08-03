# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Developer, Templates


@admin.register(Developer)


class AdminDeveloper(admin.ModelAdmin):
	list_display = ('__unicode__','id', 'name', 'age', 'bio', 'especiality', 'email', 'curriculum', 'picture')
	list_filter = ('especiality',)


@admin.register(Templates)


class AdminTemplates(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'developer', 'url', 'picture')