from django.urls import path
from .views import * 


import blog.views

urlpatterns = [
    # other patterns
    path("", blog.views.index)
]