from django.urls import path
from django_distill import distill_path
from . import views


urlpatterns = [
    path("", views.home_index, name="home_index"),
]

urlpatterns += [

    distill_path(
        '',
        views.home_index,
        name='home_index',
        distill_file='index.html'  # Home page as index.html
    ),
]
