
# Blog Post Django

A general blog post web application developed with Django in 8 version (branch)

## Installed apps:
pip install django~=4.2.13

pip install pillow

## Installed commands:
python -m venv .venv

django-admin startproject config .

python manage.py startapp blog

python manage.py startapp accounts

## Migrate commands:
python manage.py migrate

python manage.py makemigrations blog

python manage.py makemigrations accounts

## run command:
python manage.py runserver

## imported modules:
from django.urls import path, include, reverse, reverse_lazy

from django.conf import settings

from django.conf.urls.static import static

from django.views.generic import (ListView, CreateView, DetailView, UpdateView, DeleteView)

from django.db import models

from django.contrib.auth.models import AbstractUser

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from datetime import date
