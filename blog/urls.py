from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.post_detail, name="post_detail"),
    path("create/", views.post_create, name="post_create"),
    path("<int:id>/edit", views.post_edit, name="post_edit"),
]