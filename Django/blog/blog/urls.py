from django.contrib import admin
from django.urls import path
from django.urls import re_path

from firstapp import views

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    re_path(r"^about", views.about),
    path('calc/<int:num_1>/<int:num_2>/<str:symbol>/', views.calc),
    path('', views.index),
    ]
