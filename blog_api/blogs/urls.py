from django.urls import path

from . import views

urlpatterns = [
    path("blogs/", views.blog_list),
    path("blogs/<int:id>", views.blog_detail),
    path("blogs/create", views.blog_create),
]
