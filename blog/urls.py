from django.urls import path
from . import views

urlpatterns = [
    path("", view = views.starting_page, name='start-page'),
    path("posts", view= views.posts, name='posts'),
    path("posts/<slug:slug>", view= views.post_details, name='post-details')
]
