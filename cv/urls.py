from django.urls import path
from django_distill import distill_path

from . import views

# TODO slugify paths


# def get_all_blog_pks():
#     return ((post.pk,) for post in Education.objects.all())


urlpatterns = [
    path("cv/", views.cv_index, name="cv_index"),
]

urlpatterns += [

    distill_path(
        'cv/',
        views.cv_index,
        name='cv_index',
        distill_file='cv/index.html'  # Home page as index.html
    ),
]
