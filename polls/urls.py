# When the url is specified, this code will call the "views.py" file

from django.urls import path

from . import views

urlpatterns = [
    # path(route, view, kwargs, name)
    # path('PATH_NAME', function to call in views.py, name of this path)
    path('', views.index, name='index'),
]
