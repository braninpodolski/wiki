from django.urls import path

from . import views


app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.create_entry, name="create"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("random/", views.random_entry, name="random"),
    path("search/<str:query>", views.search, name="search"),
]
